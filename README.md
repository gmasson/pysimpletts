# PySimpleTTS
Conversor de texto em voz usando a API do IBM Watson™ Text to Speech e Python

### Instruções:

- Crie uma conta ou faça login no IBM cloud: 
https://cloud.ibm.com/

- Crie uma instância gratuita do serviço Text To Speech:
https://cloud.ibm.com/catalog/services/text-to-speech

- Instale a seguinte dependência no seu computador:
```
pip install ibm_watson
```
- Caso estiver usando Windows e não estiver funcionando o comando acima, tente fazer [esses passos](https://pt.stackoverflow.com/questions/239047/como-instalar-o-pip-no-windows-10)

- Edite o arquivo `converte.py` com a API Key e URL fornecidas após a criação da instância

- Edite o arquivo `texto.txt` e insira o texto que deseja converter em voz (lembrando que o limite gratuito do IBM Watson™ Text to Speech é de 10.000 caracteres por mês)

- Execute o arquivo `converte.py` e aguarde a criação do arquivo voz.mp3 dentro da pasta raiz do projeto
