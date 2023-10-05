import openai
import re

class OpenAIClient:
    def __init__(self, api_key):
        self.api_key = api_key
        openai.api_key = self.api_key

    def generar_texto(self, input_message):
        try:
            response = openai.Completion.create(
                engine="text-davinci-002",
                prompt=input_message,
                max_tokens=100
            )
            resp = response.choices[0].text.strip()
            resp = re.sub(r'[ \t,.!;:]+', ' ', resp.strip())
            resp = resp.replace('"', '')  # Elimina comillas dobles
            resp = resp.replace("'", '')  # Elimina comillas simples
            print(f"Mensaje generado: {resp}")
            return resp
        except Exception as e:
            return str(e)

