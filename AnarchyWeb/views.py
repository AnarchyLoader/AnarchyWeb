import os

from django.core.handlers.wsgi import WSGIRequest
from django.http import FileResponse, Http404, HttpResponse
from django.shortcuts import render

from AnarchyWeb.models import Hack
from Core.settings import BASE_DIR, HACKS_URL


def index(request: WSGIRequest) -> HttpResponse:
    return render(
        request,
        "index.html",
        {"hacks": Hack.objects.all(), "is_admin": request.user.is_authenticated},
    )


def send_file(request: WSGIRequest, filename):
    file_path = os.path.join(BASE_DIR, "AnarchyWeb", HACKS_URL, filename)
    if os.path.exists(file_path):
        f = open(file_path, "rb")
        return FileResponse(f, as_attachment=True)
    else:
        raise Http404("File not found")
