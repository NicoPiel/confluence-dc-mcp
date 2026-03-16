"""Qdrant client wrapper — upsert, search, and metadata filtering for chunk storage."""

# TODO: implement QdrantStore
# TODO: ensure_collection — create collection if not exists
# TODO: upsert_chunks(chunks, vectors) — deterministic UUID point IDs from page_id:chunk_index
# TODO: search(query_vector, top_k, score_threshold, space_filter) → list[dict]
# TODO: delete_by_page_id(page_id) — remove all chunks for a page (for re-indexing)
