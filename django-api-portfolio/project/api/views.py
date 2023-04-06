from rest_framework.viewsets import ModelViewSet
from project.api.serializers import ProjectSerializer
from project.models import Project
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response

from rest_framework.decorators import api_view, authentication_classes
from rest_framework.authentication import BasicAuthentication


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    @action(detail=False, methods=['delete'])
    def delete_all(self, request):
        projects = Project.objects.all()
        projects.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
