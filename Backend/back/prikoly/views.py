from rest_framework import viewsets
from .models import yo
from .serializers import yoSerializer

class yoyoset(viewsets.ModelViewSet):
    queryset = yo.objects.all()
    serializer_class = yoSerializer