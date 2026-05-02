#!/bin/bash
# Free demo — returns ~50% of one content format.
# Paid (Pro+) returns full content across 10 formats (blog, FB, LinkedIn, Twitter, email, video script, IG, thread, CTA, FAQ).
# Allowed format: twitter, linkedin, facebook, blog

curl -X POST https://cp.idea2post.app/api/v1/public/content-preview \
  -H "Content-Type: application/json" \
  -d '{
    "idea": "Why 73% of landing pages fail in the first 3 seconds",
    "format": "linkedin",
    "tone": "expert"
  }'
