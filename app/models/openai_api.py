import openai
import re


class OpenAIClient:
    def __init__(self, api_key="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"):
        self.api_key = api_key
        openai.api_key = self.api_key

    def generar_texto(self, input_message):
        try:
            response = openai.Completion.create(
                engine="text-davinci-002", prompt=input_message, max_tokens=1000
            )
            resp = response.choices[0].text.strip()
            resp = re.sub(r"[ \t,.!;:]+", " ", resp.strip())
            resp = resp.replace('"', "")  # Elimina comillas dobles
            resp = resp.replace("'", "")  # Elimina comillas simples
            print(f"Mensaje generado: {resp}")
            return resp
        except Exception as e:
            return str(e)

    def chatGpt(self, input, temperature=0.7, top_p=0.9, max_tokens=1024):
        response = openai.Completion.create(
            model="gpt-3.5-turbo-instruct",
            prompt=input,
            temperature=temperature,
            top_p=top_p,
            max_tokens=max_tokens,
        )
        print(f"mensaje para el post {response.choices[0].text.strip()}")
        return response.choices[0].text.strip()
