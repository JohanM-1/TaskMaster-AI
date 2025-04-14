from unittest.mock import MagicMock
from unittest.mock import patch

from django.conf import settings
from django.test import TestCase
from openai import OpenAIError

from app_documents.ai_config import OpenAIClient


class OpenAIConfigTests(TestCase):
    def test_api_key_loaded(self):
        """Verifica que la API key esté configurada correctamente"""
        self.assertTrue(
            hasattr(settings, "OPENAI_API_KEY"),
            "OPENAI_API_KEY no está en la configuración de Django",
        )
        self.assertIsNotNone(settings.OPENAI_API_KEY, "OPENAI_API_KEY está vacío")
        self.assertNotEqual(
            settings.OPENAI_API_KEY, "", "OPENAI_API_KEY no debe ser un string vacío"
        )


class OpenAIAPITests(TestCase):
    def setUp(self):
        self.client = OpenAIClient()

    def test_successful_connection(self):
        """Test de conexión básica a la API"""
        try:
            # Prueba simple de listar modelos
            models = self.client.client.models.list()
            self.assertIsNotNone(models)
        except Exception as e:
            self.fail(f"Falló la conexión a la API: {str(e)}")

    def test_invalid_request(self):
        """Test de manejo de errores"""
        with self.assertRaises(Exception) as context:
            # Enviar un request inválido
            self.client.get_chat_completion("", model="modelo-inexistente")

        self.assertIn("Error", str(context.exception))

    def test_authentication_error(self):
        """Test de autenticación fallida"""
        # Guardar temporalmente la key válida
        original_key = settings.OPENAI_API_KEY
        try:
            # Forzar una key inválida
            settings.OPENAI_API_KEY = "sk-invalid-key"
            with self.assertRaises(Exception) as context:
                client = OpenAIClient()
                client.get_chat_completion("test")

            self.assertIn("Authentication", str(context.exception))
        finally:
            # Restaurar la key original
            settings.OPENAI_API_KEY = original_key

    @patch("openai.OpenAI")
    def test_send_message(self, mock_openai):
        # Configurar el mock
        mock_response = MagicMock()
        mock_response.choices = [MagicMock(message=MagicMock(content="Test response"))]
        mock_response.usage = MagicMock(_asdict=lambda: {"total_tokens": 10})
        mock_openai.return_value.chat.completions.create.return_value = mock_response

        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": "cuanto es 1 + 1 solo responde 2 si esta es la repuesta",
            },
        ]

        response = self.client.send_message(
            messages=messages, model="gpt-4", temperature=0.8, max_tokens=100
        )

        self.assertEqual(response["status"], "success")
        self.assertEqual(response["content"], "2")
        self.assertIsNotNone(response["usage"])

    def test_send_message_with_different_models(self):
        """Test envío de mensajes a diferentes modelos"""
        messages = [{"role": "user", "content": "Test message"}]

        # Probar con GPT-4
        try:
            response = self.client.send_message(messages, model="gpt-4")
            self.assertEqual(response["status"], "success")
        except Exception as e:
            if "not available" in str(e).lower():
                self.skipTest("GPT-4 no está disponible para esta cuenta")

        # Probar con GPT-3.5-turbo
        response = self.client.send_message(messages, model="gpt-3.5-turbo")
        self.assertEqual(response["status"], "success")
