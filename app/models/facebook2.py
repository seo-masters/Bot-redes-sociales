import facebook
import requests



class FacebookAPI2:
    def __init__(self):
        pass

    def obtener_access_token(self):
        app_id = 'TU_APP_ID'
        app_secret = 'TU_APP_SECRET'
        code = 'EL_CODIGO_DE_AUTORIZACION'

        token_url = f'https://graph.facebook.com/v12.0/oauth/access_token?client_id={app_id}&client_secret={app_secret}&code={code}&grant_type=fb_exchange_token'
        response = requests.get(token_url)
        data = response.json()

        if 'access_token' in data:
            long_lived_access_token = data['access_token']
            print(f'Token de Acceso de Largo Plazo: {long_lived_access_token}')
        else:
            print('No se pudo obtener el Token de Acceso de Largo Plazo')





