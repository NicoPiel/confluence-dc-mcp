"""CLI entrypoint for manual or cron-triggered Confluence indexing crawls."""

# TODO: implement CLI with typer
# TODO: crawl command — full_reindex flag
#   - load Settings from config
#   - instantiate ConfluenceClient, EmbeddingClient, QdrantStore
#   - call crawl_and_index
#   - print CrawlReport summary
