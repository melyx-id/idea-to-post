# Idea2Post API Reference

> Full reference at https://idea2post.app/api (tier-gated). This Markdown is a quick overview.

**Base URL:** `https://cp.idea2post.app/api/v1`

## Authentication

| Endpoint family | Auth |
|---|---|
| `/v1/public/*` | None — IP rate-limited 3/day |
| All others | `Authorization: Bearer i2p_live_...` (Agency plan) |

Generate tokens at <https://cp.idea2post.app/?page=account>.

---

## Free demo endpoints

### `POST /v1/public/hook-suggest`

```json
{ "idea": "5 mistakes coaches make on landing pages", "tone": "expert" }
```

Returns 3 hooks (vs paid 10-20 + scoring + chat refine).

### `POST /v1/public/content-preview`

```json
{
  "idea": "Why 73% of landing pages fail in the first 3 seconds",
  "format": "linkedin",
  "tone": "expert"
}
```

Returns ~50% of one format (vs paid full content × 10 formats).

Allowed formats: `twitter`, `linkedin`, `facebook`, `blog`.

---

## Paid endpoints (Pro+ / Agency)

| Endpoint | Tier | Purpose |
|---|---|---|
| `POST /v1/hooks` | Pro+ | 10-20 viral hooks + score |
| `POST /v1/content` | Pro+ | 10 formats: blog, FB, LinkedIn, Twitter, email, video script, IG, thread, CTA, FAQ |
| `POST /v1/series` | Pro+ | Generate 5-30 post series in a theme |
| `POST /v1/projects` | Pro+ | Manage content projects |
| `POST /v1/competitors/scan` | Pro+ | Track competitor accounts |
| `POST /v1/publish/facebook` | Agency | Auto-publish FB |
| `POST /v1/publish/linkedin` | Agency | Auto-publish LinkedIn |
| `POST /v1/auto-pipeline` | Agency | Full auto-publish orchestration |

Full schemas at <https://idea2post.app/api> (login + paid required).

---

## Errors

```json
{
  "ok": false,
  "error": "rate_limit_exceeded",
  "kind": "rate_limit",
  "detail": "3 calls/day from this IP. Reset at 00:00 UTC.",
  "upgrade_url": "https://cart.melyx.id/pay/idea2post-pro"
}
```
