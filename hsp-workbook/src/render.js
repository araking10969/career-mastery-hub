const { chromium } = require('/opt/node-tools/node_modules/playwright');
const path = require('path');
(async () => {
  const dir = __dirname;
  const out = process.argv[2];
  const b = await chromium.launch();
  const p = await b.newPage();
  await p.goto('file://' + path.join(dir, 'workbook.html'));
  await p.evaluate(() => document.fonts.ready);
  // overflow check: any element inside .pin extending beyond .pin bottom
  const issues = await p.evaluate(() => {
    const r = [];
    document.querySelectorAll('.page').forEach((pg, i) => {
      const pin = pg.querySelector('.pin');
      const pb = pin.getBoundingClientRect().bottom;
      let max = 0;
      pin.querySelectorAll('*').forEach(e => { const b = e.getBoundingClientRect().bottom; if (b > max) max = b; });
      const foot = pg.querySelector('.pfoot');
      const limit = foot ? foot.getBoundingClientRect().top : pg.getBoundingClientRect().bottom;
      r.push(`p${i + 1}: content bottom ${(max - pg.getBoundingClientRect().top) / 3.7795 | 0}mm, limit ${(limit - pg.getBoundingClientRect().top) / 3.7795 | 0}mm${max > limit ? '  <<< OVERFLOW' : ''}`);
    });
    return r;
  });
  console.log(issues.join('\n'));
  await p.pdf({ path: out, format: 'A4', printBackground: true, preferCSSPageSize: true });
  await b.close();
})();
