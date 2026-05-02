# Idea-to-Post

> Turn 1 idea into 10+ pieces of content — hooks, blog, email, LinkedIn, Twitter, video script — programmatically.

[![Built with Claude](https://img.shields.io/badge/Built%20with-Claude-7c3aed?logo=anthropic)](https://www.anthropic.com/claude)
[![API Status](https://img.shields.io/badge/API-live-success)](https://cp.idea2post.app)
[![Free trial](https://img.shields.io/badge/Free%20trial-3%20calls%2Fday-22c55e)](https://cp.idea2post.app)

**Idea-to-Post** is a hosted AI platform: paste an idea (or YouTube link, or document) and get 10+ ready-to-publish content formats in 30 seconds.

This repo contains the **public API documentation, SDK examples, and demo notebooks**. The hosted SaaS engine (multi-format generation, FB/LinkedIn auto-publish, content series planning, competitor tracking) runs at [cp.idea2post.app](https://cp.idea2post.app).

---

## ✨ What you can build

| Use case | Endpoint family | Tier |
|---|---|---|
| 10-20 viral hooks per idea | `/v1/hooks` | Pro+ |
| Multi-format content (blog, FB, LinkedIn, Twitter, email, video script, IG, thread, CTA, FAQ) | `/v1/content` | Pro+ |
| Content series (5-30 posts in a theme) | `/v1/series` | Pro+ |
| Auto-publish to FB / LinkedIn | `/v1/publish/*` | Agency |
| Competitor tracking + viral pulls | `/v1/competitors/scan` | Pro+ |
| Auto-pipeline orchestration | `/v1/auto-pipeline` | Agency |

**Free tier** = 3 calls/day on demo endpoints (truncated/watermarked output). Paid plans: full quota + watermark removal + multi-format unlock.

---

## 🚀 Quick start (free, no signup)

```bash
curl -X POST https://cp.idea2post.app/api/v1/public/hook-suggest \
  -H "Content-Type: application/json" \
  -d '{
    "idea": "5 mistakes coaches make on landing pages",
    "tone": "expert"
  }'
```

Response:

```json
{
  "ok": true,
  "hooks": [
    {"style": "viral", "hook": "I pasted 1 link into AI...", "score": 92},
    {"style": "curiosity", "hook": "90% of coaches make this exact mistake...", "score": 88},
    {"style": "story", "hook": "My landing page got 0 leads...", "score": 85}
  ],
  "watermark": "Powered by idea2post.app — upgrade for 10-20 hooks + scoring",
  "calls_remaining_today": 2
}
```

---

## 📦 SDKs

- **Python** — see [`examples/python/`](examples/python/)
- **Node.js** — see [`examples/node/`](examples/node/)
- **cURL** — see [`examples/curl/`](examples/curl/)

---

## 🎬 Demo

Try it without signup at [Hugging Face Space →](https://huggingface.co/spaces/melyx/idea-to-post) (rate-limited, watermarked).

---

## 📚 Docs

- [Full API reference (tier-gated)](https://idea2post.app/api)
- [Pricing & quotas](docs/pricing.md)
- [API quickstart](docs/api.md)

---

## 💼 Pricing

| Plan | Monthly | API calls | API tokens | Auto-publish |
|---|---|---|---|---|
| Free trial | $0 | 3/day | — | — |
| Pro | $39 | 500/mo | — | — |
| Agency | $199 | 5,000/mo | 3 tokens | ✓ FB + LinkedIn |
| Empire | $499 | 20,000/mo | unlimited | ✓ all platforms |

[Upgrade →](https://cart.melyx.id/pay/idea2post-pro)

---

## 🔐 License

This repository (docs, examples, SDK stubs) is licensed under [MIT](LICENSE).
The hosted API service is proprietary; usage is subject to [Terms of Service](https://idea2post.app/terms).

---

## 🛠 Built with

- **Backend**: PHP 8.4 + MySQL (multi-tenant workspace isolation)
- **AI orchestration**: OpenAI GPT-4o, fal.ai (image generation), Whisper (transcription)
- **Auto-publish**: Facebook Graph API, LinkedIn API
- **Developed with**: [Anthropic Claude](https://www.anthropic.com/claude) AI assistance throughout

---

## 📬 Support

- Issues / questions: [open an issue](https://github.com/melyx-id/idea-to-post/issues)
- Email: support@idea2post.app
- Made by [melyx.dev](https://melyx.dev)
