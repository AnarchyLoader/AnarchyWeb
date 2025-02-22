from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render

from AnarchyWeb.models import Hack


def index(request: WSGIRequest) -> HttpResponse:
    return render(
        request,
        "index.html",
        {
            "hacks": Hack.objects.all(),
            "is_admin": request.user.is_authenticated,
            "admin_username": request.user.get_username(),
        },
    )
