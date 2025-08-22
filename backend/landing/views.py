from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet
from .models import Header, Summary, Project
from .serializers import HeaderSerializer, SummarySerializer, ProjectSerializer

class HeaderView(APIView):
    def get(self, request):
        header = Header.objects.first()
        serializer = HeaderSerializer(header, context={'request': request})
        return Response(serializer.data)


class SummaryViewSet(viewsets.ModelViewSet):
    queryset = Summary.objects.all()
    serializer_class = SummarySerializer

class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all().order_by("-id")
    serializer_class = ProjectSerializer