// Idea2Post Node.js SDK — minimal client.
//
// Free tier: no apiKey. 3 calls/day per IP.
// Paid tier: apiKey (Agency) for full multi-format access.

export class Idea2Post {
  constructor({ apiKey = null, baseUrl = 'https://cp.idea2post.app/api/v1' } = {}) {
    this.apiKey = apiKey;
    this.baseUrl = baseUrl.replace(/\/$/, '');
  }

  // Free demo
  hookSuggest(idea, tone = 'expert') { return this._post('/public/hook-suggest', { idea, tone }, false); }
  contentPreview(idea, format = 'twitter', tone = 'expert') {
    return this._post('/public/content-preview', { idea, format, tone }, false);
  }

  // Paid
  hooks(opts) { return this._post('/hooks', opts); }
  content(opts) { return this._post('/content', opts); }
  series(opts) { return this._post('/series', opts); }
  publishFacebook(opts) { return this._post('/publish/facebook', opts); }
  publishLinkedin(opts) { return this._post('/publish/linkedin', opts); }
  competitorsScan(opts) { return this._post('/competitors/scan', opts); }

  async _post(path, body, auth = true) {
    const headers = { 'Content-Type': 'application/json', 'User-Agent': 'idea2post-node/0.1' };
    if (auth) {
      if (!this.apiKey) throw new Error('apiKey required (Agency) — get one at cp.idea2post.app');
      headers.Authorization = `Bearer ${this.apiKey}`;
    }
    const r = await fetch(this.baseUrl + path, { method: 'POST', headers, body: JSON.stringify(body) });
    const txt = await r.text();
    let data;
    try { data = JSON.parse(txt); }
    catch { throw new Error(`Non-JSON response (${r.status}): ${txt.substring(0, 200)}`); }
    if (!r.ok || data.ok === false) throw new Error(`HTTP ${r.status}: ${data.error || JSON.stringify(data)}`);
    return data;
  }
}

if (import.meta.url === `file://${process.argv[1]}`) {
  const ip = new Idea2Post();
  console.log(await ip.hookSuggest('How to start a side hustle'));
}
