// Vercel Serverless Function: GET /api/rate
// API 키는 Vercel 환경변수 EXCHANGE_RATE_API_KEY 에만 있고 브라우저로 나가지 않습니다.
module.exports = async (req, res) => {
  const key = process.env.EXCHANGE_RATE_API_KEY;
  if (!key) return res.status(500).json({ error: 'EXCHANGE_RATE_API_KEY is not set' });
  try {
    const r = await fetch(`https://v6.exchangerate-api.com/v6/${key}/pair/USD/KRW`);
    const j = await r.json();
    if (j.result !== 'success') return res.status(502).json({ error: j['error-type'] || 'upstream error' });
    // 1시간 캐시 → 무료 플랜 호출 한도 절약
    res.setHeader('Cache-Control', 's-maxage=3600, stale-while-revalidate=86400');
    return res.status(200).json({
      base: 'USD', quote: 'KRW',
      rate: j.conversion_rate,
      date: new Date(j.time_last_update_unix * 1000).toISOString().slice(0, 10),
      source: 'ExchangeRate-API'
    });
  } catch (e) {
    return res.status(502).json({ error: 'fetch failed' });
  }
};
