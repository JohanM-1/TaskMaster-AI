from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


# Clase base para las versiones
class VersionBase(models.Model):
    version = models.PositiveIntegerField(default=1)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    promt = models.CharField(null=True, blank=True, max_length=2555)

    class Meta:
        abstract = True


# Modelos principales con el campo 'version'
class Project(models.Model):
    name = models.CharField(null=True, blank=True, max_length=255)
    problem = models.CharField(null=True, blank=True, max_length=2555)
    promt = models.CharField(null=True, blank=True, max_length=2555)
    version = models.PositiveIntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.pk:  # Si el projecto ya existe, incrementar la versión
            self.version += 1
        super().save(*args, **kwargs)


class Requerimientos(models.Model):
    description = models.TextField()
    version = models.PositiveIntegerField(default=1)
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, default=None
    )  # Reference project

    def save(self, *args, **kwargs):
        if self.pk:
            self.version += 1
        super().save(*args, **kwargs)


class UserHistory(models.Model):
    history = models.TextField()
    version = models.PositiveIntegerField(default=1)
    requerimientos = models.ForeignKey(
        Requerimientos, on_delete=models.CASCADE, default=None
    )

    def save(self, *args, **kwargs):
        if self.pk:
            self.version += 1
        super().save(*args, **kwargs)


class Task(models.Model):
    title = models.CharField(max_length=255)
    version = models.PositiveIntegerField(default=1)
    user_history = models.ForeignKey(
        UserHistory, on_delete=models.CASCADE, default=None
    )

    def save(self, *args, **kwargs):
        if self.pk:
            self.version += 1
        super().save(*args, **kwargs)


# Modelos de versionado basados en la clase abstracta
class VersionProject(VersionBase):
    name = models.CharField(null=True, blank=True, max_length=255)
    problem = models.CharField(null=True, blank=True, max_length=2555)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)


class VersionRequerimientos(VersionBase):
    requerimiento = models.ForeignKey(Requerimientos, on_delete=models.CASCADE)


class VersionUserHistory(VersionBase):
    user_history = models.ForeignKey(UserHistory, on_delete=models.CASCADE)


class VersionTask(VersionBase):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
