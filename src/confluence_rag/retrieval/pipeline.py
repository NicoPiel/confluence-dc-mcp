"""Query pipeline — embed query → Qdrant search → permission filter → return context."""

# TODO: implement RetrievalConfig dataclass (top_k, top_k_after_filter, score_threshold, space_filter)
# TODO: implement ScoredChunk dataclass (content, metadata, score)
# TODO: implement RetrievalResult dataclass (chunks, user_identity, total_candidates, filtered_count)
# TODO: implement retrieve(query, user_email, embedder, qdrant, permissions, config) → RetrievalResult
#   1. resolve user email → UserIdentity (cached)
#   2. embed query
#   3. search Qdrant for top_k candidates
#   4. batch permission check on unique page IDs
#   5. filter chunks to accessible pages
#   6. return top_k_after_filter by score
