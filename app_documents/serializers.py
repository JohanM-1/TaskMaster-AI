from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from rest_framework import serializers

from .models import Project
from .models import Requerimientos
from .models import Task
from .models import UserHistory
from .models import VersionProject
from .models import VersionRequerimientos
from .models import VersionTask
from .models import VersionUserHistory

User = get_user_model()


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]


class ProjectoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ["url", "name", "problem", "version", "promt", "user"]


class VersionProjectoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VersionProject
        fields = ["url", "name", "problem", "version", "project", "promt"]


class RequerimientosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Requerimientos
        fields = ["url", "description", "version"]


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ["url", "title", "version"]
