"""Unit tests for PermissionResolver."""

# TODO: test resolve_user_identity — email → UserIdentity mapping
# TODO: test resolve_user_identity — cache hit (second call doesn't hit API)
# TODO: test check_page_access — no restrictions → allowed
# TODO: test check_page_access — user in restricted_users → allowed
# TODO: test check_page_access — user's group in restricted_groups → allowed
# TODO: test check_page_access — user not in any restriction → denied
# TODO: test filter_accessible_pages — mixed allowed/denied pages
