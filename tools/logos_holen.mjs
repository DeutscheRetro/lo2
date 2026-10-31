// Einmalig: Wappen der 18 Zweitligisten von OpenLigaDB holen und als 120-px-PNG nach logos/ legen.
import { chromium } from '/Users/andreaslenski/Downloads/Ligaoutsider-Spot/node_modules/playwright-core/index.mjs'
import { writeFileSync, readFileSync } from 'node:fs'
const teams = JSON.parse(readFileSync(process.argv[2], 'utf-8'))
const exe = process.env.HOME + '/Library/Caches/ms-playwright/chromium-1243/chrome-mac-arm64/Google Chrome for Testing.app/Contents/MacOS/Google Chrome for Testing'
const b = await chromium.launch({ executablePath: exe })
const p = await b.newPage({ viewport: { width: 140, height: 140 }, deviceScaleFactor: 1 })
for (const [slug, url] of Object.entries(teams)) {
  try {
    const r = await fetch(url, { headers: { 'User-Agent': 'Ligaoutsider-Logo-Import/1.0 (+https://ligaoutsider.de)' } })
    const typ = r.headers.get('content-type') || ''
    const buf = Buffer.from(await r.arrayBuffer())
    const src = `data:${typ.split(';')[0] || 'image/png'};base64,${buf.toString('base64')}`
    await p.setContent(`<body style="margin:0;background:transparent;display:flex;align-items:center;justify-content:center;width:140px;height:140px"><img src="${src}" style="max-width:120px;max-height:120px;object-fit:contain"></body>`)
    await p.waitForTimeout(150)
    writeFileSync(`logos/${slug}.png`, await p.screenshot({ omitBackground: true, clip: { x: 10, y: 10, width: 120, height: 120 } }))
    console.log('ok', slug, typ.split(';')[0], buf.length)
  } catch (e) { console.log('FEHLER', slug, e.message.slice(0, 60)) }
}
await b.close()
