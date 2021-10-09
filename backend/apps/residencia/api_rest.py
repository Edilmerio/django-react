from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from .models import Edificio
from .serializers import EdificioSerializer

class ListEdificios(ListAPIView):
    queryset = Edificio.objects.all()
    serializer_class = EdificioSerializer