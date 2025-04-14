from django.db.models.signals import post_save
from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import Project  # Asegúrate de importar después de crear los modelos
from .models import Requerimientos  # Asegúrate de importar después de crear los modelos
from .models import Task  # Asegúrate de importar después de crear los modelos
from .models import UserHistory  # Asegúrate de importar después de crear los modelos
from .models import VersionProject  # Asegúrate de importar después de crear los modelos
from .models import (  # Asegúrate de importar después de crear los modelos
    VersionRequerimientos,
)
from .models import VersionTask  # Asegúrate de importar después de crear los modelos
from .models import (  # Asegúrate de importar después de crear los modelos
    VersionUserHistory,
)
from .tasks import create_project_structure  # Ajusta según tu estructura real


# Señales para crear versiones después de cada actualización
@receiver(post_save, sender=Project)
def crear_version_projecto(sender, instance, **kwargs):
    VersionProject.objects.create(
        project=instance,
        version=instance.version,
        name=instance.name,
        problem=instance.problem,
        promt=instance.promt,
    )
    create_project_structure(instance)


@receiver(post_save, sender=Requerimientos)
def crear_version_requerimiento(sender, instance, **kwargs):
    VersionRequerimientos.objects.create(
        requerimiento=instance, version=instance.version
    )


@receiver(post_save, sender=UserHistory)
def crear_version_user_history(sender, instance, **kwargs):
    VersionUserHistory.objects.create(user_history=instance, version=instance.version)


@receiver(post_save, sender=Task)
def crear_version_task(sender, instance, **kwargs):
    VersionTask.objects.create(task=instance, version=instance.version)
