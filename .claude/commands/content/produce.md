# Produce

End-to-end content production pipeline. Takes an article from brief through publish-ready, or runs individual stages.

```
/produce                          # Interactive — assess what's ready, suggest next step
/produce brief <keyword>          # Stage 1: Generate content brief
/produce write <brief-file>       # Stage 2: Write article from brief
/produce qc <article-file>        # Stage 3: SEO/AEO quality check
/produce images <article-file>    # Stage 4: Generate feature image + social graphics
/produce publish <article-file>   # Stage 5: Push to CMS + generate social + push to scheduler
/produce all <keyword>            # Run stages 1-5 sequentially with checkpoints
```

---

## Pipeline Stages

```
Stage 1          Stage 2         Stage 3         Stage 4           Stage 5
/content-brief → /writing      → /seo-qc       → templated_renderer → /publish
   keyword         brief           draft           article              article
   ↓               ↓               ↓               ↓                    ↓
   brief.md        article.md      scorecard       feature-image.png    CMS draft
                                   + fixes         social-graphics.png  Social drafts
```

---

## Stage 1: Content Brief

Run `/cmo/content/content-brief` with the target keyword.

**Input:** keyword or topic
**Output:** `content/briefs/{keyword-slug}-brief.md`
**Checkpoint:** Show brief to user, confirm before writing.

---

## Stage 2: Write Article

Run `/cmo/content/writing` with the brief as context.

**Input:** brief file from Stage 1
**Output:** `content/{content-type}-{date}.md`
**Checkpoint:** User reviews draft before QC.

---

## Stage 3: SEO/AEO Quality Check

Run `/cmo/content/seo-qc` on the draft.

**Input:** article file from Stage 2
**Output:** Scorecard (SEO score, AEO score, Content Quality score) + fix recommendations
**Action:** Apply recommended fixes, re-run QC until score > 80.
**Checkpoint:** Show final scores, confirm ready for images.

---

## Stage 4: Generate Images

```bash
# Generate feature image
python3 tools/templated_renderer.py --render <article-file>

# Check result
python3 tools/image_resolver.py --resolve <slug>
```

**Input:** article file (reads title + content_type from frontmatter)
**Output:** `content/images/{slug}-{type}.png`
**Checkpoint:** If no template exists for this content type, tell user which template to build in Templated.io.

---

## Stage 5: Publish

Run `/cmo/distribution/publish` with the article.

This handles:
1. Push article to CMS as draft (with feature image if available)
2. Generate social post variants (LinkedIn + Twitter)
3. Push social posts to scheduler as drafts with images

**Input:** article file
**Output:** CMS draft URL + scheduled post count
**Final checkpoint:** Tell user to review in CMS admin and scheduler dashboard before scheduling.

---

## Interactive Mode

When invoked as just `/produce` with no arguments:

1. Check `content/` for files with frontmatter `status: draft` or `status: wip`
2. Check `content/briefs/` for unwritten briefs
3. Check image manifest for missing images
4. Suggest the most useful next action:
   - "You have 2 briefs without articles → run `/produce write`"
   - "You have 1 article that hasn't been QC'd → run `/produce qc`"
   - "You have 3 articles ready but no images → run `/produce images`"
   - "You have 1 article ready to publish → run `/produce publish`"

---

## File Routing

| Stage | Output Location |
|---|---|
| Brief | `content/briefs/{keyword-slug}-brief.md` |
| Article | `content/{content-type}-{date}.md` |
| Images | `content/images/{slug}-{type}.png` |
| Social posts | Generated at publish time, pushed directly to scheduler |
| CMS draft | Created via API, URL returned |
