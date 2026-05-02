#!/bin/bash
# Free demo — no auth, 3 calls/day per IP, returns 3 hooks.
# Paid (Pro+) returns 10-20 hooks with viral score + chat refinement.

curl -X POST https://cp.idea2post.app/api/v1/public/hook-suggest \
  -H "Content-Type: application/json" \
  -d '{
    "idea": "5 mistakes coaches make on landing pages",
    "tone": "expert"
  }'
