from rest_framework import routers, serializers, viewsets

from AnarchyWeb.models import Hack


class HackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hack
        fields = [
            "id",
            "name",
            "description",
            "author",
            "status",
            "process",
            "file",
            "source",
            "game",
            "working",
        ]


class HackViewSet(viewsets.ModelViewSet):
    queryset = Hack.objects.all()
    serializer_class = HackSerializer


router = routers.DefaultRouter()
router.register(r"hacks", HackViewSet)
