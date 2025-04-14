import json
import logging
import re

from celery import shared_task
from django.db import transaction

from .ai_config import OpenAIClient
from .models import Project
from .models import Requerimientos
from .models import Task
from .models import UserHistory

logger = logging.getLogger(__name__)


def generate_project_prompt(project: Project):
    return [
        {
            "role": "user",
            "content": f"""Please analyze this project and generate a structured response with:
        Project Name: {project.name}
        Project Problem: {project.problem}
        
        Generate a JSON response with the following structure:
        {{
            "requirements": [
                {{
                    "description": "requirement description",
                    "user_stories": [
                        {{
                            "description": "user story description",
                            "tasks": [
                                {{
                                    "title": "task title"
                                }}
                            ]
                        }}
                    ]
                }}
            ]
        }}
        
                    IMPORTANTE:
            - Usa siempre comillas dobles.
            - No incluyas caracteres inválidos como \\n o \\t.
            - Si un campo es texto, escapa las comillas dobles internas con \\".
            - Nunca agregues contenido fuera del JSON.
        """,
        }
    ]


@shared_task(bind=True, max_retries=3)
def generate_project_data(self, project: Project):
    try:
        ai_client = OpenAIClient()

        messages = generate_project_prompt(project)
        response = ai_client.send_message(
            messages=messages, temperature=0.7, max_tokens=2000
        )

        if response["status"] == "success":
            parsed_response = json.loads(response["content"])
            return parsed_response  # Devuelve el diccionario
        else:
            raise self.retry(countdown=60)

    except project.DoesNotExist:
        logger.error(f"projecto {project.id} no encontrado")
        return None
    except Exception as e:
        logger.error(f"Error generando datos AI: {str(e)}")
        raise self.retry(exc=e)


@shared_task
def create_project_structure(project: Project):
    try:
        # Ejecutar generate_project_data y esperar su resultado
        ai_data = generate_project_data(project=project)
        if (
            not ai_data
            or not isinstance(ai_data, dict)
            or "requirements" not in ai_data
        ):
            logger.error(
                "El formato de los datos AI generados es inválido o está vacío para el projecto %s",  # noqa: E501
                project.id,
            )
            raise Exception("Datos AI inválidos")

        with transaction.atomic():
            # Crear requerimientos
            for req_data in ai_data.get("requirements", []):
                req = Requerimientos.objects.create(
                    description=req_data["description"],
                    project=project,
                )

                # Crear historias de usuario
                for history_data in req_data.get("user_stories", []):
                    history = UserHistory.objects.create(
                        history=history_data["description"],
                        requerimientos=req,
                    )

                    # Crear tareas
                    for task_data in history_data.get("tasks", []):
                        Task.objects.create(
                            title=task_data["title"],
                            user_history=history,
                        )

            logger.info("Estructura del projecto %s creada exitosamente", project.id)

    except Exception as e:
        logger.exception("Error creando estructura del projecto %s", project.id)
        raise
