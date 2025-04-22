# downloads/views.py
import os
import datetime
from urllib.parse import unquote
from django.conf import settings
from django.shortcuts import render
from django.http import Http404

BASE_DIR = "/var/www/labportal/sw-dumps"

def list_downloads(request, subpath=""):
    # Prevent path traversal
    requested_path = os.path.normpath(os.path.join(BASE_DIR, subpath))
    if not requested_path.startswith(BASE_DIR):
        raise Http404("Invalid path")

    if not os.path.exists(requested_path):
        raise Http404("Path not found")

    entries = []
    try:
        for name in sorted(os.listdir(requested_path)):
            full_path = os.path.join(requested_path, name)
            is_dir = os.path.isdir(full_path)
            stat = os.stat(full_path)
            entries.append({
                "name": name,
                "is_dir": is_dir,
                "size": stat.st_size if not is_dir else None,
                "modified": datetime.datetime.fromtimestamp(stat.st_mtime),
                "link": f"/downloads/{subpath}{name}/" if is_dir else f"/sw-dumps/{subpath}{name}",
            })
    except Exception as e:
        entries = []

    # Breadcrumb navigation
    parts = subpath.strip("/").split("/") if subpath else []
    breadcrumbs = []
    for i in range(len(parts)):
        breadcrumb_path = "/".join(parts[:i+1]) + "/"
        breadcrumbs.append((parts[i], breadcrumb_path))

    return render(request, "downloads/list.html", {
        "entries": entries,
        "breadcrumbs": breadcrumbs,        
    })
