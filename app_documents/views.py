import logging

from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.shortcuts import redirect
from django.shortcuts import render
from rest_framework import permissions
from rest_framework import viewsets

from app_documents.serializers import GroupSerializer
from app_documents.serializers import ProjectoSerializer
from app_documents.serializers import UserSerializer
from app_documents.serializers import VersionProjectoSerializer

from .models import Project
from .models import VersionProject

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Group.objects.all().order_by("name")
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProjectoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows projectos to be viewed or edited.
    """

    queryset = Project.objects.all()
    serializer_class = ProjectoSerializer
    permission_classes = [permissions.IsAuthenticated]


class VersionProjectoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows version projectos to be viewed or edited.
    """

    queryset = VersionProject.objects.all()
    serializer_class = VersionProjectoSerializer
    permission_classes = [permissions.IsAuthenticated]


@login_required
def crear_projecto(request):
    if request.method == "POST":
        name = request.POST.get("name")
        problem = request.POST.get("problem")
        promt = request.POST.get("promt")
        nuevo_projecto = Project(
            name=name,
            problem=problem,
            promt=promt,
            user=request.user,
        )
        nuevo_projecto.save()
        return redirect("list_projects")
    return render(request, "manage/edit_project.html")


@login_required
def view_project(request, project_id):
    project = Project.objects.get(id=project_id, user=request.user)
    return render(request, "manage/view_project.html", {"project": project})


@login_required
def edit_project(request, project_id):
    project = Project.objects.get(id=project_id, user=request.user)
    if request.method == "POST":
        project.name = request.POST.get("name")
        project.problem = request.POST.get("problem")
        project.promt = request.POST.get("promt")
        project.save()
        return redirect("list_projects")
    return render(request, "manage/edit_project.html", {"project": project})


@login_required
def list_projects(request):
    logger = logging.getLogger(__name__)
    projects = Project.objects.filter(user=request.user)

    logger.info(f"Number of projects: {projects.count()}")

    for project in projects:
        logger.info(
            f"Project ID: {project.id}, Name: {project.name}, Problem: {project.problem}, Prompt: {project.promt}"
        )

    return render(request, "manage/list_projects.html", {"projects": projects})
