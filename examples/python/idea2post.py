"""
Idea2Post Python SDK — minimal client.

Free tier: no api_key. 3 calls/day per IP, output truncated/watermarked.
Paid tier: api_key (Agency plan) for full multi-format access.

Usage:
    from idea2post import Idea2Post

    ip = Idea2Post()
    print(ip.hook_suggest("5 mistakes coaches make on landing pages"))
    print(ip.content_preview("Why 73% of landing pages fail", format="linkedin"))

    paid = Idea2Post(api_key="i2p_live_...")
    res = paid.hooks(idea="...", count=15)
"""
from __future__ import annotations
import json
import urllib.request
import urllib.error
from typing import Optional, Any, List

BASE_URL = "https://cp.idea2post.app/api/v1"


class Idea2PostError(Exception):
    pass


class Idea2Post:
    def __init__(self, api_key: Optional[str] = None, base_url: str = BASE_URL):
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")

    # ─── Free demo ────────────────────────────────────────────
    def hook_suggest(self, idea: str, tone: str = "expert") -> dict:
        return self._post("/public/hook-suggest", {"idea": idea, "tone": tone}, auth=False)

    def content_preview(self, idea: str, format: str = "twitter", tone: str = "expert") -> dict:
        return self._post("/public/content-preview",
                          {"idea": idea, "format": format, "tone": tone},
                          auth=False)

    # ─── Paid endpoints ───────────────────────────────────────
    def hooks(self, idea: str, count: int = 10, styles: Optional[List[str]] = None,
              tone: str = "expert") -> dict:
        return self._post("/hooks", {
            "idea": idea, "count": count,
            "styles": styles or ["viral", "curiosity", "story"],
            "tone": tone,
        })

    def content(self, idea: str, formats: List[str], tone: str = "expert",
                language: str = "en", audience: Optional[str] = None) -> dict:
        return self._post("/content", {
            "idea": idea, "formats": formats, "tone": tone,
            "language": language, "audience": audience,
        })

    def series(self, theme: str, count: int = 10, format: str = "linkedin") -> dict:
        return self._post("/series", {"theme": theme, "count": count, "format": format})

    def publish_facebook(self, page_id: str, message: str,
                         image_url: Optional[str] = None,
                         schedule_at: Optional[str] = None) -> dict:
        return self._post("/publish/facebook", {
            "page_id": page_id, "message": message,
            "image_url": image_url, "schedule_at": schedule_at,
        })

    def publish_linkedin(self, message: str,
                         schedule_at: Optional[str] = None) -> dict:
        return self._post("/publish/linkedin", {
            "message": message, "schedule_at": schedule_at,
        })

    def competitors_scan(self, accounts: List[str]) -> dict:
        return self._post("/competitors/scan", {"accounts": accounts})

    # ─── HTTP helpers ─────────────────────────────────────────
    def _headers(self, auth: bool) -> dict:
        h = {"Content-Type": "application/json", "Accept": "application/json",
             "User-Agent": "idea2post-python/0.1"}
        if auth:
            if not self.api_key:
                raise Idea2PostError("api_key required (Agency plan) — get one at cp.idea2post.app/?page=account")
            h["Authorization"] = f"Bearer {self.api_key}"
        return h

    def _post(self, path: str, body: Any, auth: bool = True) -> dict:
        req = urllib.request.Request(self.base_url + path,
                                     data=json.dumps(body).encode("utf-8"),
                                     headers=self._headers(auth),
                                     method="POST")
        return self._send(req)

    @staticmethod
    def _send(req) -> dict:
        try:
            with urllib.request.urlopen(req, timeout=120) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            try:
                detail = json.loads(e.read().decode("utf-8"))
            except Exception:
                detail = {"error": str(e)}
            raise Idea2PostError(f"HTTP {e.code}: {detail}") from e


if __name__ == "__main__":
    ip = Idea2Post()
    print(json.dumps(ip.hook_suggest("How to start a side hustle"), indent=2, ensure_ascii=False))
