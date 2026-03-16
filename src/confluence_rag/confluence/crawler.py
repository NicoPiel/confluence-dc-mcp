"""Indexing pipeline — crawl Confluence spaces, extract content, chunk, and embed."""

# TODO: implement CrawlConfig dataclass
# TODO: implement CrawlReport dataclass
# TODO: implement crawl_and_index coroutine
#   - fetch all pages in configured spaces (paginated)
#   - incremental mode: skip pages not modified since last crawl
#   - for each page: extract → chunk → embed → upsert to Qdrant
#   - bounded concurrency via asyncio.Semaphore
#   - per-page error handling (don't abort on single failure)
