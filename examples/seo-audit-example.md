# SEO Audit Example Output

This is an example of what `/seo-audit` produces. Names and data are fictional.

---

## SEO Audit Report

**Client:** Acme SaaS Inc.
**Domain:** acmesaas.com
**Date:** 2026-02-15
**Data Sources:** Google Search Console, Google Analytics 4

---

## Executive Summary

| Category | Score | Status |
|----------|-------|--------|
| Technical SEO | 78/100 | Needs Attention |
| Content Quality | 72/100 | Needs Attention |
| Keyword Performance | 65/100 | Significant Issues |
| Backlink Profile | 81/100 | Good |
| **Overall** | **74/100** | **Needs Attention** |

**Key Finding:** Strong domain authority but underperforming on high-intent commercial keywords. Technical issues on product pages limiting crawl efficiency.

---

## Traffic Overview (Last 90 Days)

| Metric | Current | vs Prior Period | vs Prior Year |
|--------|---------|-----------------|---------------|
| Organic Sessions | 45,230 | +8.2% | +23.4% |
| Organic Clicks (GSC) | 52,100 | +5.1% | +18.7% |
| Impressions | 1.2M | +12.3% | +45.2% |
| Average Position | 18.4 | -1.2 (worse) | +3.1 (better) |
| CTR | 4.3% | -0.3% | +0.2% |

---

## Critical Issues

### 1. Core Web Vitals Failing on Product Pages

**Pages Affected:** 23 product pages (78% of product catalog)

| Metric | Current | Target | Status |
|--------|---------|--------|--------|
| LCP | 4.2s | <2.5s | Fail |
| INP | 320ms | <200ms | Fail |
| CLS | 0.08 | <0.1 | Pass |

**Impact:** Poor mobile rankings, reduced crawl budget
**Fix:** Optimize hero images, defer non-critical JS, implement lazy loading

### 2. Duplicate Content on Filtered URLs

**Issue:** Product category pages with filters creating duplicate content
**URLs Affected:** ~2,400 parameter variations
**Example:** `/products?color=blue` duplicates `/products`

**Fix:**
- Add canonical tags pointing to base URL
- Use robots meta noindex on filtered pages
- Or implement proper URL parameter handling in GSC

---

## High Priority Opportunities

### 3. Position 4-10 Keywords (Quick Wins)

Keywords ranking positions 4-10 with high commercial intent:

| Keyword | Position | Volume | URL |
|---------|----------|--------|-----|
| "best [product] software" | 6 | 2,400 | /best-[product] |
| "[product] for enterprise" | 8 | 1,800 | /enterprise |
| "[product] pricing" | 5 | 3,200 | /pricing |
| "compare [product] tools" | 7 | 890 | /comparisons |
| "[product] vs [competitor]" | 9 | 1,200 | /vs-[competitor] |

**Opportunity:** Moving these to top 3 = estimated +5,400 monthly clicks
**Action:** Content optimization, internal linking, fresh updates

### 4. Missing H1 Tags on Key Pages

**Pages Affected:** 8 high-traffic pages
- /features (12K monthly sessions)
- /integrations (8K monthly sessions)
- /security (5K monthly sessions)

**Fix:** Add descriptive H1 tags with target keywords

---

## Content Recommendations

### Thin Content Pages

| URL | Word Count | Sessions | Bounce Rate |
|-----|------------|----------|-------------|
| /features/analytics | 234 | 890 | 72% |
| /integrations/zapier | 156 | 2,100 | 68% |
| /use-cases/marketing | 312 | 650 | 75% |

**Recommendation:** Expand to 1,500+ words with:
- Detailed feature explanations
- Use case examples
- Screenshots/videos
- FAQ section

### Content Gap Analysis

Keywords competitors rank for that you don't:

| Keyword | Competitor | Volume | Difficulty |
|---------|------------|--------|------------|
| "[product] tutorial" | Competitor A | 4,200 | Medium |
| "how to [use case]" | Competitor B | 3,800 | Low |
| "[product] certification" | Competitor A | 1,200 | Low |
| "[industry] automation guide" | Competitor C | 2,900 | Medium |

---

## Technical SEO Checklist

| Item | Status | Notes |
|------|--------|-------|
| XML Sitemap | ✓ | 2,340 URLs indexed |
| Robots.txt | ✓ | Properly configured |
| HTTPS | ✓ | Full site |
| Mobile-Friendly | ✓ | All pages pass |
| Core Web Vitals | ✗ | 23 pages failing |
| Structured Data | ⚠ | Missing on product pages |
| Canonical Tags | ⚠ | Missing on filtered URLs |
| Hreflang | ✓ | EN/ES/FR configured |
| Internal Linking | ⚠ | Orphan pages detected |

---

## Backlink Profile

| Metric | Value | Industry Benchmark |
|--------|-------|-------------------|
| Domain Rating | 58 | 55 (above avg) |
| Referring Domains | 1,240 | 1,000 (above avg) |
| Dofollow % | 72% | 65% (above avg) |
| Toxic Links | 3% | <5% (healthy) |

**Top Linking Domains:**
1. TechCrunch (DR 94)
2. Product Hunt (DR 91)
3. G2 (DR 89)
4. Capterra (DR 86)
5. Industry Blog A (DR 72)

---

## 90-Day Action Plan

### Month 1: Technical Foundation

- [ ] Fix Core Web Vitals on product pages
- [ ] Implement canonical tags on filtered URLs
- [ ] Add H1 tags to 8 affected pages
- [ ] Add structured data (Product, FAQ) to product pages

### Month 2: Content Optimization

- [ ] Expand 3 thin content pages to 1,500+ words
- [ ] Optimize 5 position 4-10 keywords
- [ ] Create 2 content gap pieces (tutorial, guide)
- [ ] Update internal linking to orphan pages

### Month 3: Growth & Measurement

- [ ] Launch link building campaign for new content
- [ ] A/B test title tags on high-impression pages
- [ ] Monitor Core Web Vitals improvements
- [ ] Re-audit and measure impact

---

## Expected Impact

| Metric | Current | 90-Day Target | Growth |
|--------|---------|---------------|--------|
| Organic Sessions | 45,230 | 58,000 | +28% |
| Position 4-10 Keywords | 42 | 25 | -40% (to top 3) |
| Core Web Vitals Pass Rate | 22% | 90% | +68% |
| Organic Conversions | 1,240 | 1,600 | +29% |

---

*Generated by Growth Marketer AI Toolkit — `/seo-audit`*
