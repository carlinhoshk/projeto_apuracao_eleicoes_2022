# 02/10/2022 

import requests
import json
import pandas


# usando request get para puxar o json lá do TSE
data = requests.get('https://resultados.tse.jus.br/oficial/ele2022/544/dados-simplificados/br/br-c0001-e000544-r.json')

#montando a estrutura do json para ser tratado pela repetição 
json_data = json.loads(data.content)

#criando variaveis vazias para serem fomentadas com dados do json
canditado = []
partido = []
votos = []
porcentagem = []

#fomentando informações para estrutura json
for informacoes in json_data['cand']:
    if informacoes['seq'] in ['1','2','3','4']:
        canditado.append(informacoes['nm'])
        votos.append(informacoes['vap'])
        porcentagem.append(informacoes['pvap'])

#Pandas para plotar todas informações unidas
df_eleicao = pandas.DataFrame(list(zip(canditado, votos, porcentagem)), columns= ['Candidato', 'Nº de Votos', 'Porcentagem'])

print(df_eleicao)