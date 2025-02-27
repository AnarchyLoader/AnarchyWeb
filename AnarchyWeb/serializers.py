from rest_framework import routers, serializers, viewsets

from AnarchyWeb.models import Hack
from rest_framework import serializers


class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        fields = kwargs.pop("fields", None)
        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)
        if fields is not None:
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)


class HackSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Hack
        fields = "__all__"


class HackViewSet(viewsets.ModelViewSet):
    queryset = Hack.objects.all()
    serializer_class = HackSerializer


router = routers.DefaultRouter()
router.register(r"hacks", HackViewSet)
