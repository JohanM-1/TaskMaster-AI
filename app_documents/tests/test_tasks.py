import json
from unittest.mock import patch

from django.test import TestCase

from app_documents.models import Project
from app_documents.tasks import create_project_structure


class ProjectStructureTest(TestCase):
    def setUp(self):
        self.project = Project.objects.create(
            name="Test Project", problem="Test Problem"
        )

        self.mock_ai_response = {
            "requirements": [
                {
                    "description": "Create a login system for users",
                    "user_stories": [
                        {
                            "description": "As a user, I want to be able to log in to my account",
                            "tasks": [
                                {"title": "Implement login form"},
                                {"title": "Validate user credentials"},
                                {"title": "Create session for logged in user"},
                            ],
                        },
                        {
                            "description": "As a user, I want to be able to reset my password",
                            "tasks": [
                                {"title": "Implement password reset functionality"},
                                {"title": "Send password reset link to user's email"},
                            ],
                        },
                    ],
                },
                {
                    "description": "Implement a messaging feature for users",
                    "user_stories": [
                        {
                            "description": "As a user, I want to be able to send messages to other users",
                            "tasks": [
                                {"title": "Create messaging interface"},
                                {"title": "Implement message sending functionality"},
                                {"title": "Display received messages in inbox"},
                            ],
                        },
                        {
                            "description": "As a user, I want to be notified of new messages",
                            "tasks": [
                                {"title": "Implement message notification system"},
                                {"title": "Notify user of new messages in real-time"},
                            ],
                        },
                    ],
                },
            ]
        }

    def test_generate_project_data_structure(self):
        # Llamar a la función REAL (sin mocks)
        from app_documents.tasks import generate_project_data

        result = generate_project_data(self.project)

        # Verificar que la respuesta no está vacía
        self.assertIsNotNone(result)

        # Imprimir la respuesta generada para inspección
        print("Generated Result:", json.dumps(result, indent=2))

        # Validar estructura básica del JSON
        self.assertIsInstance(result, dict)
        self.assertIn("requirements", result)
        self.assertIsInstance(result["requirements"], list)

        # Validar estructura de un requerimiento
        requirement = result["requirements"][0]
        self.assertIn("description", requirement)
        self.assertIn("user_stories", requirement)
        self.assertIsInstance(requirement["user_stories"], list)

        # Validar estructura de una historia de usuario
        user_story = requirement["user_stories"][0]
        self.assertIn("description", user_story)
        self.assertIn("tasks", user_story)
        self.assertIsInstance(user_story["tasks"], list)

        # Validar estructura de una tarea
        task = user_story["tasks"][0]
        self.assertIn("title", task)

        self.assertTrue(requirement["description"].strip())
        self.assertTrue(user_story["description"].strip())
        self.assertTrue(task["title"].strip())

    @patch("app_documents.tasks.generate_project_data")
    def test_create_project_structure(self, mock_generate_data):
        # Configure the mock to return our test data
        mock_generate_data.return_value = self.mock_ai_response

        # Execute create_project_structure
        create_project_structure(project=self.project)

        # Verify requirements were created
        self.assertEqual(self.project.requerimientos_set.count(), 2)

        # Verify first requirement and its structure
        first_req = self.project.requerimientos_set.first()
        self.assertEqual(first_req.description, "Create a login system for users")
        self.assertEqual(first_req.userhistory_set.count(), 2)

        # Verify first user story and its tasks
        first_story = first_req.userhistory_set.first()
        self.assertEqual(
            first_story.history, "As a user, I want to be able to log in to my account"
        )
        self.assertEqual(first_story.task_set.count(), 3)

        # Verify tasks of first user story
        tasks = first_story.task_set.all()
        expected_tasks = [
            "Implement login form",
            "Validate user credentials",
            "Create session for logged in user",
        ]
        self.assertEqual([task.title for task in tasks], expected_tasks)
