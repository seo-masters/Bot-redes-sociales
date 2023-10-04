import openai

class OpenAIClient:
    def __init__(self, api_key):
        self.api_key = api_key
        openai.api_key = self.api_key

    def generar_texto(self, input_message):
        try:
            response = openai.Completion.create(
                engine="text-davinci-002",
                prompt=input_message,
                max_tokens=50
            )
            resp = response.choices[0].text.strip()
            print(f"Mensaje generado: {resp}")
            return resp
        except Exception as e:
            return str(e)

