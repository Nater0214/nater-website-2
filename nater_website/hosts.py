from django.contrib import admin
from django_hosts import host, patterns

import root

host_patterns = patterns(
    '',
    host(r"", root.urls, name="root"),
    host(r"admin", admin.site.urls, name="admin")
)