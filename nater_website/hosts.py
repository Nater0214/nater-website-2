from django_hosts import host, patterns

host_patterns = patterns(
    '',
    host(r"", "root.urls", name="root"),
    host(r"admin", "admin.site.urls", name="admin")
)