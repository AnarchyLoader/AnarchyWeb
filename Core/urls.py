from django.contrib import admin
from django.urls import include, path, re_path
from django.views.static import serve

from AnarchyWeb import serializers
from AnarchyWeb.views import *
from Core.settings import STATIC_ROOT

urlpatterns = [
    path("admin/", admin.site.urls),

    path('api/', include(serializers.router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
    path("", index),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': STATIC_ROOT})
]
