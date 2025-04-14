from typing import Any
from typing import Dict
from typing import List
from typing import Optional

import openai
from django.conf import settings
from openai import OpenAIError


class OpenAIClient:
    def __init__(self):
        self.api_key = settings.OPENAI_API_KEY
        self.client = openai.OpenAI(api_key=self.api_key)

    def get_chat_completion(self, prompt, model="gpt-3.5-turbo"):
        try:
            response = self.client.chat.completions.create(
                model=model, messages=[{"role": "user", "content": prompt}]
            )
            return response.choices[0].message.content
        except OpenAIError as e:
            # Manejar diferentes tipos de errores
            error_message = f"OpenAI API Error: {str(e)}"
            if isinstance(e, openai.AuthenticationError):
                error_message = "Authentication Error: Invalid API Key"
            elif isinstance(e, openai.APIConnectionError):
                error_message = "Connection Error: Failed to connect to OpenAI API"

            # Podrías loggear el error aquí
            raise Exception(error_message) from e

    def send_message(
        self,
        messages: List[Dict[str, str]],
        model: str = "gpt-3.5-turbo",
        temperature: float = 0.7,
        max_tokens: Optional[int] = None,
    ) -> Dict[str, Any]:
        """
        Envía mensajes al modelo especificado con configuraciones personalizadas.

        Args:
            messages: Lista de mensajes en formato [{"role": "user", "content": "mensaje"}, ...]
            model: Modelo a utilizar (default: gpt-3.5-turbo)
            temperature: Nivel de creatividad (0-1)
            max_tokens: Máximo de tokens en la respuesta
        """
        try:
            response = self.client.chat.completions.create(
                model=model,
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens,
            )
            return {
                "status": "success",
                "content": response.choices[0].message.content,
                "usage": response.usage if hasattr(response, "usage") else None,
            }
        except OpenAIError as e:
            error_message = f"OpenAI API Error: {str(e)}"
            if isinstance(e, openai.AuthenticationError):
                error_message = "Authentication Error: Invalid API Key"
            elif isinstance(e, openai.APIConnectionError):
                error_message = "Connection Error: Failed to connect to OpenAI API"
            raise Exception(error_message) from e
