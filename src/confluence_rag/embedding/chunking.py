"""Text chunking strategies — heading-aware splitting and sliding window."""

# TODO: implement ChunkMetadata dataclass
#   (page_id, page_title, space_key, heading_path, chunk_index, page_version,
#    page_last_modified, labels)
# TODO: implement Chunk dataclass (text, metadata)
# TODO: implement extract_and_chunk(page, max_chunk_tokens, overlap) → list[Chunk]
#   - parse Confluence XHTML with BeautifulSoup + lxml
#   - split on h1/h2/h3, preserve heading hierarchy as metadata
#   - sliding window for sections exceeding max_chunk_tokens
