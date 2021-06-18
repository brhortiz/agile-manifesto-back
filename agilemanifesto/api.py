from rest_framework import generics

from .models import AgilePrinciple, AgileValue
from .serializers import AgilePrincipleSerializer, AgileValueSerializer

#Principle
class AgilePrincipleList(generics.ListAPIView):
    queryset = AgilePrinciple.objects.exclude(is_deleted=True)[:12]
    serializer_class = AgilePrincipleSerializer


class CreateAgilePrinciple(generics.CreateAPIView):
    queryset = AgilePrinciple.objects.all()
    serializer_class = AgilePrincipleSerializer


class UpdateAgilePrinciple(generics.UpdateAPIView):
    queryset = AgilePrinciple.objects.all()
    serializer_class = AgilePrincipleSerializer


class DeleteAgilePrinciple(generics.DestroyAPIView):
    queryset = AgilePrinciple.objects.all()
    serializer_class = AgilePrincipleSerializer

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()


#Value
class AgileValueList(generics.ListAPIView):
    queryset = AgileValue.objects.exclude(is_deleted=True)[:4]
    serializer_class = AgileValueSerializer


class CreateAgileValue(generics.CreateAPIView):
    queryset = AgileValue.objects.all()
    serializer_class = AgileValueSerializer


class UpdateAgileValue(generics.UpdateAPIView):
    queryset = AgileValue.objects.all()
    serializer_class = AgileValueSerializer


class DeleteAgileValue(generics.DestroyAPIView):
    queryset = AgileValue.objects.all()
    serializer_class = AgileValueSerializer

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()