#!/usr/bin/env python3
"""
LLM Router Tool
---------------
Routes prompts to appropriate LLM providers (OpenAI or Anthropic) based on
task type configuration. Provides fallback behavior when primary model fails.

Usage:
    # From command line
    python llm_router.py --task insight_generation --prompt "Analyze these metrics..."
    python llm_router.py --test  # Run test suite

    # From Python
    from tools.llm_router import route_task
    response = route_task("insight_generation", "Analyze these metrics...")

Configuration:
    Create a model-routing-config.json file with your model preferences.
    See the CONFIG_PATH variable below for expected location.
"""

import argparse
import json
import os
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Optional

# Load environment variables from .env
def load_env():
    """Load environment variables from .env file."""
    env_path = Path(__file__).parent.parent / ".env"
    if env_path.exists():
        with open(env_path, 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    key, _, value = line.partition('=')
                    key = key.strip()
                    value = value.strip().strip('"').strip("'")
                    os.environ.setdefault(key, value)

load_env()

# Configuration paths - customize for your project structure
CONFIG_PATH = Path(__file__).parent.parent / "config" / "model-routing-config.json"

# Default configuration if no config file exists
DEFAULT_CONFIG = {
    "default_model": "claude",
    "models": {
        "claude": {
            "provider": "anthropic",
            "api_model_id": "claude-sonnet-4-20250514",
            "max_tokens": 4096,
            "temperature": 0.7
        },
        "gpt-4": {
            "provider": "openai",
            "api_model_id": "gpt-4",
            "max_tokens": 4096,
            "temperature": 0.7
        }
    },
    "task_routing": {
        "insight_generation": {"model": "claude", "provider": "anthropic"},
        "narrative_writing": {"model": "claude", "provider": "anthropic"},
        "code_generation": {"model": "gpt-4", "provider": "openai"}
    }
}


@dataclass
class RoutingResult:
    """Result from an LLM routing call."""
    success: bool
    content: str
    model_used: str
    provider: str
    fallback_used: bool
    error: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        return {
            "success": self.success,
            "content": self.content,
            "model_used": self.model_used,
            "provider": self.provider,
            "fallback_used": self.fallback_used,
            "error": self.error
        }


def load_config() -> Dict[str, Any]:
    """Load routing configuration from JSON file or use defaults."""
    if CONFIG_PATH.exists():
        with open(CONFIG_PATH, 'r') as f:
            return json.load(f)
    else:
        # Return default config if no file exists
        return DEFAULT_CONFIG


def call_openai(prompt: str, model_config: Dict[str, Any], system_prompt: Optional[str] = None) -> str:
    """
    Call OpenAI API with the given prompt.

    Args:
        prompt: The user prompt to send
        model_config: Model configuration dict with api_model_id, max_tokens, temperature
        system_prompt: Optional system prompt for context

    Returns:
        The response text from the model

    Raises:
        Exception: If API call fails
    """
    try:
        from openai import OpenAI
    except ImportError:
        raise ImportError("OpenAI package not installed. Run: pip install openai")

    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY not found in environment")

    client = OpenAI(api_key=api_key)

    messages = []
    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})
    messages.append({"role": "user", "content": prompt})

    response = client.chat.completions.create(
        model=model_config.get("api_model_id", "gpt-4"),
        messages=messages,
        max_tokens=model_config.get("max_tokens", 4096),
        temperature=model_config.get("temperature", 0.7)
    )

    return response.choices[0].message.content


def call_anthropic(prompt: str, model_config: Dict[str, Any], system_prompt: Optional[str] = None) -> str:
    """
    Call Anthropic API with the given prompt.

    Args:
        prompt: The user prompt to send
        model_config: Model configuration dict with api_model_id, max_tokens, temperature
        system_prompt: Optional system prompt for context

    Returns:
        The response text from the model

    Raises:
        Exception: If API call fails
    """
    try:
        import anthropic
    except ImportError:
        raise ImportError("Anthropic package not installed. Run: pip install anthropic")

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        raise ValueError("ANTHROPIC_API_KEY not found in environment")

    client = anthropic.Anthropic(api_key=api_key)

    kwargs = {
        "model": model_config.get("api_model_id", "claude-sonnet-4-20250514"),
        "max_tokens": model_config.get("max_tokens", 4096),
        "messages": [{"role": "user", "content": prompt}]
    }

    if system_prompt:
        kwargs["system"] = system_prompt

    response = client.messages.create(**kwargs)

    return response.content[0].text


def route_task(
    task_type: str,
    prompt: str,
    system_prompt: Optional[str] = None,
    allow_fallback: bool = True
) -> RoutingResult:
    """
    Route a task to the appropriate LLM based on configuration.

    Args:
        task_type: Type of task (e.g., "insight_generation", "narrative_writing")
        prompt: The prompt to send to the model
        system_prompt: Optional system prompt for context
        allow_fallback: Whether to fall back to default model on failure

    Returns:
        RoutingResult with response content and metadata
    """
    config = load_config()

    # Get task routing config
    task_routing = config.get("task_routing", {})
    task_config = task_routing.get(task_type)

    if not task_config:
        # Use default model if task type not found
        model_name = config.get("default_model", "claude")
        task_config = {
            "model": model_name,
            "provider": config.get("models", {}).get(model_name, {}).get("provider", "anthropic")
        }

    model_name = task_config.get("model")
    model_config = config.get("models", {}).get(model_name, {})
    provider = task_config.get("provider", model_config.get("provider", "anthropic"))

    # Try primary model
    try:
        if provider == "openai":
            content = call_openai(prompt, model_config, system_prompt)
        else:
            content = call_anthropic(prompt, model_config, system_prompt)

        return RoutingResult(
            success=True,
            content=content,
            model_used=model_name,
            provider=provider,
            fallback_used=False
        )

    except Exception as primary_error:
        error_msg = str(primary_error)

        # If fallback is disabled, return error
        if not allow_fallback:
            return RoutingResult(
                success=False,
                content="",
                model_used=model_name,
                provider=provider,
                fallback_used=False,
                error=error_msg
            )

        # Try fallback to default model
        default_model = config.get("default_model", "claude")
        if default_model == model_name:
            # Already using default, can't fall back
            return RoutingResult(
                success=False,
                content="",
                model_used=model_name,
                provider=provider,
                fallback_used=False,
                error=error_msg
            )

        # Attempt fallback
        try:
            default_config = config.get("models", {}).get(default_model, {})
            default_provider = default_config.get("provider", "anthropic")

            if default_provider == "openai":
                content = call_openai(prompt, default_config, system_prompt)
            else:
                content = call_anthropic(prompt, default_config, system_prompt)

            return RoutingResult(
                success=True,
                content=content,
                model_used=default_model,
                provider=default_provider,
                fallback_used=True,
                error=f"Primary model failed: {error_msg}. Fell back to {default_model}."
            )

        except Exception as fallback_error:
            return RoutingResult(
                success=False,
                content="",
                model_used=model_name,
                provider=provider,
                fallback_used=True,
                error=f"Primary ({error_msg}) and fallback ({fallback_error}) both failed."
            )


def generate_insights(
    metrics: Dict[str, Any],
    context: str = "",
    scope: str = "overall",
    system_prompt: Optional[str] = None
) -> RoutingResult:
    """
    Generate strategic insights from metrics data.

    This is a convenience function that formats metrics for insight generation
    and routes to the appropriate model.

    Args:
        metrics: Dictionary of metric names to values
        context: Additional context about the reporting period
        scope: Analysis scope (e.g., "overall", "segment")
        system_prompt: Custom system prompt (default provided if None)

    Returns:
        RoutingResult with generated insights
    """
    # Format metrics for prompt
    metrics_text = "\n".join([f"- {k}: {v}" for k, v in metrics.items()])

    if system_prompt is None:
        system_prompt = """You are a growth analytics expert analyzing engagement metrics.
Your role is to identify strategic insights and actionable observations from the data.

Focus on:
1. Performance vs benchmarks and prior periods
2. Trends that indicate opportunities or risks
3. Specific, actionable recommendations

Be direct and concise. Use bullet points. Prioritize insights by impact."""

    user_prompt = f"""Analyze the following {scope} engagement metrics and provide strategic insights:

{context}

**Metrics:**
{metrics_text}

Provide 3-5 key insights with:
- Observation (what the data shows)
- Implication (what it means)
- Recommendation (what to do)"""

    return route_task("insight_generation", user_prompt, system_prompt)


def run_tests():
    """Run basic tests to verify routing configuration and API connectivity."""
    print("\n=== LLM Router Test Suite ===\n")

    # Test 1: Load config
    print("Test 1: Loading configuration...")
    try:
        config = load_config()
        print(f"  OK: Config loaded with {len(config.get('models', {}))} models defined")
        print(f"      Task types: {list(config.get('task_routing', {}).keys())}")
    except Exception as e:
        print(f"  FAIL: {e}")
        return 1

    # Test 2: Check environment variables
    print("\nTest 2: Checking API keys...")
    openai_key = os.environ.get("OPENAI_API_KEY")
    anthropic_key = os.environ.get("ANTHROPIC_API_KEY")

    if openai_key:
        print(f"  OK: OPENAI_API_KEY found ({openai_key[:8]}...)")
    else:
        print("  WARN: OPENAI_API_KEY not found - OpenAI routing will fail")

    if anthropic_key:
        print(f"  OK: ANTHROPIC_API_KEY found ({anthropic_key[:8]}...)")
    else:
        print("  WARN: ANTHROPIC_API_KEY not found - Anthropic routing will fail")

    # Test 3: Test routing logic (without API call)
    print("\nTest 3: Testing routing logic...")
    for task_type in ["insight_generation", "narrative_writing", "unknown_task"]:
        task_routing = config.get("task_routing", {})
        task_config = task_routing.get(task_type, {"model": config.get("default_model", "claude")})
        model = task_config.get("model", config.get("default_model", "claude"))
        print(f"  {task_type} -> {model}")

    # Test 4: API connectivity (optional, requires keys)
    print("\nTest 4: API connectivity (dry run)...")
    print("  Skipping live API tests. Run with --test-live to test actual API calls.")

    print("\n=== Tests Complete ===\n")
    return 0


def run_live_tests():
    """Run live API tests (requires valid API keys)."""
    print("\n=== LLM Router Live Tests ===\n")

    test_prompt = "In one sentence, what is 2+2?"
    config = load_config()

    # Test OpenAI
    print("Test: OpenAI API...")
    try:
        model_config = config.get("models", {}).get("gpt-4", {})
        response = call_openai(test_prompt, model_config)
        print(f"  OK: {response[:100]}...")
    except Exception as e:
        print(f"  FAIL: {e}")

    # Test Anthropic
    print("\nTest: Anthropic API...")
    try:
        model_config = config.get("models", {}).get("claude", {})
        response = call_anthropic(test_prompt, model_config)
        print(f"  OK: {response[:100]}...")
    except Exception as e:
        print(f"  FAIL: {e}")

    # Test full routing
    print("\nTest: Full routing (insight_generation)...")
    result = route_task("insight_generation", test_prompt)
    if result.success:
        print(f"  OK: Routed to {result.model_used} ({result.provider})")
        print(f"      Fallback used: {result.fallback_used}")
        print(f"      Response: {result.content[:100]}...")
    else:
        print(f"  FAIL: {result.error}")

    print("\n=== Live Tests Complete ===\n")


def main():
    parser = argparse.ArgumentParser(description="LLM Router Tool")
    parser.add_argument("--task", type=str, help="Task type to route")
    parser.add_argument("--prompt", type=str, help="Prompt to send")
    parser.add_argument("--system", type=str, help="Optional system prompt")
    parser.add_argument("--test", action="store_true", help="Run test suite")
    parser.add_argument("--test-live", action="store_true", help="Run live API tests")
    parser.add_argument("--output", choices=["json", "text"], default="text", help="Output format")
    args = parser.parse_args()

    if args.test:
        return run_tests()

    if args.test_live:
        run_live_tests()
        return 0

    if not args.task or not args.prompt:
        parser.print_help()
        print("\nError: --task and --prompt are required for routing")
        return 1

    result = route_task(args.task, args.prompt, args.system)

    if args.output == "json":
        print(json.dumps(result.to_dict(), indent=2))
    else:
        if result.success:
            print(f"\n[{result.model_used}] Response:")
            print("-" * 40)
            print(result.content)
            if result.fallback_used:
                print(f"\n(Note: {result.error})")
        else:
            print(f"\nError: {result.error}")
            return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
