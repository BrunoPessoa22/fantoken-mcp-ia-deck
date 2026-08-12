# Esporte, Fan Token, MCP e IA — Keynote deck

Deck for Bruno Pessoa's keynote at the **AI Stage, Blockchain.Rio 2026** (ExpoRio, Rio de Janeiro — Aug 12 2026, 16:15–16:40, Day 1). Content in PT-BR, Chiliz brand system. 16 slides, 1280×720, pure HTML/CSS — no framework. Copy is deliberately sparse — key talking points only; Bruno narrates the detail live.

- **Live:** https://keynote.brunopessoa.com
- **`esporte-fantoken-mcp-ia.pdf`** — the sendable/AV-desk deliverable (exact 1280×720 pages).
- **`index.html`** — the built deck. Arrow keys / space / click to navigate; `#N` in the URL jumps to slide N. Fully self-contained (fonts + logo inlined).
- **`deck.tpl.html`** — the editable source. All copy and styles live here. Placeholders `__CHILIZ__` and `/*__FONTFACE__*/` are filled by the build.
- **`build.py`** — inlines `assets/` into the template → writes `index.html`.
- **`assets/`** — embedded font CSS (Space Grotesk / Manrope / Space Mono, OFL) and the Chiliz logo data URI.

## Editing workflow

1. Edit `deck.tpl.html` (never `index.html` — it's generated).
2. Rebuild: `python3 build.py`
3. Regenerate the PDF:
   ```bash
   "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
     --headless=new --disable-gpu --no-pdf-header-footer \
     --print-to-pdf="$PWD/esporte-fantoken-mcp-ia.pdf" "file://$PWD/index.html"
   ```
4. Push to `main` → redeploy the Coolify app.

## Narrative arc

1. **O ativo** — what a Fan Token™ is; the asset whose catalysts (matches) are public weeks ahead (440 measured matchdays, post-draw drift).
2. **O protocolo** — what MCP is; Fan Token Intel as the first fan-token MCP server (120+ tools, odds tape incl. the 2026 WC final).
3. **O agente** — agentic trading; "the LLM proposes, code decides" risk architecture; the honest war stories (WC-final post-mortem, first agent-executed fan-token perp). The whale-signal 50.8% slide was cut per Bruno (Aug 12) — keep that data out of the deck.
4. **A fusão** — x402 agent payments on the OKX OnchainOS marketplace; the full loop: match → data → thesis → gate → execution.
5. **Novidade (slide 16)** — Fan Tokens™ live on Solana (official Chiliz registry, LayerZero OFT, 10 tradeable as of Jul 2026, SPAIN/ARG/PSG most liquid), the cross-chain data opportunity for the FTI MCP, the Solana-ready roadmap, and a QR code (segno-generated, `assets/qr_datauri.txt`) pointing to fantokenintel.com.

## Content notes

- All figures come from Fan Token Intel production data and published post-mortems (Jun–Jul 2026): post-draw −1.7%/24h (n=463); 23.7K odds ticks; 1,052 minute-resolution abnormal-return events; 19 x402 SKUs settling in USDT0 on X Layer; first agent-executed fan-token perp long+short (PSG on vibe.trading, Jul 22 2026, $3 test capital).
- Every slide with market data carries an educational / not-investment-advice source line.
- Brand: Chiliz palette (Midnight `#1D0238`, Eclipse `#40006A`, Pepper `#FF0051`, Meta Spark `#CF85FF`, Layer Zero `#EDEDED`), Space Grotesk headlines / Manrope body / Space Mono term-sheet voice (approved slides-context fallbacks for Atyp Text / PP Mori), no gradient text, deck legibility standard (dim .80 / faint .56).
