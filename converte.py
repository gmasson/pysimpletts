# PySimpleTTS
# Conversor de texto em voz usando a API do IBM Watson™ Text to Speech e Python

# Importando as dependências
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# Chaves da API (insira suas chaves dentro das variáveis abaixo)
apikey = 'SUA API KEY AQUI'
url = 'SUA URL AQUI'

# Autenticando
authenticator = IAMAuthenticator(apikey)
tts = TextToSpeechV1(authenticator=authenticator)
tts.set_service_url(url)

# Lendo o texto
with open('texto.txt', 'r', encoding='utf-8') as f:
    text = f.readlines()
text = [line.replace('\n','') for line in text]
text = ''.join(str(line) for line in text)

# Convertendo texto em voz (voz feminina da rede neural)
with open('./voz.mp3', 'wb') as audio_file:
    res = tts.synthesize(text, accept='audio/mp3', voice='pt-BR_IsabelaV3Voice').get_result()
    audio_file.write(res.content)
