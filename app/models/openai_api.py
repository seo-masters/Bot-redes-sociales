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

    def chatGpt(
        self, input, sin_emogi=False, temperature=0.7, top_p=0.9, max_tokens=1024
    ):
        response = openai.Completion.create(
            model="gpt-3.5-turbo-instruct",
            prompt=input,
            temperature=temperature,
            top_p=top_p,
            max_tokens=max_tokens,
        )
        print(f"mensaje para el post {response.choices[0].text.strip()}")
        if sin_emogi:
            mensaje = re.sub(
                r"[\U0001F600-\U0001F64F\U0001F300-\U0001F5FF\U0001F680-\U0001F6FF\U0001F700-\U0001F77F\U0001F780-\U0001F7FF\U0001F800-\U0001F8FF\U0001F900-\U0001F9FF\U0001FA00-\U0001FA6F\U0001FA70-\U0001FAFF\U0001FB00-\U0001FBFF\U0001FC00-\U0001FCFF\U0001FD00-\U0001FDFF\U0001FE00-\U0001FEFF\U0001FF00-\U0001FFFF\U00002000-\U0000206F\U00002100-\U000027BF\U00002B05\U00002B06\U00002B07\U00002B1B\U00002B50\U00002B06\U000023E9\U000023F0\U00002B05\U0001F004\U0001F0CF\U00002B05\U00002B06\U00002B07\U00002B1B\U00002B50\U00002B06\U000023E9\U000023F0\U00002B05\U0001F004\U0001F0CF]+",
                "",
                response.choices[0].text.strip(),
            )
            return mensaje.strip('"')
        else:
            return response.choices[0].text.strip().strip('"')
            
