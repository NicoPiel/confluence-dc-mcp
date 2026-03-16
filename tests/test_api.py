"""API endpoint tests using FastAPI TestClient."""

# TODO: test POST /api/v1/retrieve — valid request → 200 with chunks
# TODO: test POST /api/v1/retrieve — unknown email → 403 or empty result
# TODO: test GET  /api/v1/health — Confluence and Qdrant reachable → 200
# TODO: test GET  /api/v1/health — Confluence unreachable → 503
# TODO: test POST /api/v1/index/trigger — triggers crawl, returns job ID
# TODO: test GET  /api/v1/index/status — returns last crawl report
