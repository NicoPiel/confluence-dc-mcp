"""Permission resolver — maps AD emails to Confluence identities and checks page access."""

# TODO: implement PermissionResolver using cachetools.TTLCache
# TODO: resolve_user_identity(email) → UserIdentity  (cached, TTL 15 min)
# TODO: check_page_access(page_id, user) → bool
#   - fetch page restrictions
#   - if no restrictions → inherited space perms → allow
#   - if restrictions → check username + group intersection
# TODO: filter_accessible_pages(page_ids, user) → list[str]
#   - parallel restriction fetches via ThreadPoolExecutor
