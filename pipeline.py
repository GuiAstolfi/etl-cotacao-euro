import requests
import pandas as pd
from sqlalchemy import create_engine
import time

def extract():

    url = 'https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL'
    response = requests.get(url= url)
    dados = response.json()
    dados_EUR = [dados['EURBRL']]
    df = pd.DataFrame(dados_EUR)
    return df

def transform(dados):

    dados = dados.rename(columns= {'codein': 'transformação', 
                                   'high': 'valor máximo', 
                                   'low': 'valor mínimo', 
                                   'pctChange': 'comparação anterior', 
                                   'create_date': 'data da conversão', 
                                   'name': 'nome', 
                                   'code': 'código'})
    dados['nome'] = dados['nome'].replace('Euro/Real Brasileiro', 'EURO')
    dados = dados[['data da conversão', 'nome', 'código', 'transformação', 'valor máximo', 'valor mínimo', 'comparação anterior']]
    return dados

def load(df):
    engine = create_engine('sqlite:///cotacao_euro.db')
    df.to_sql('cotacao_euro', con= engine, if_exists= 'append', index= False)

def rodar_etl():
    df = extract()
    df = transform(df)
    load(df)
    print('dados salvos com sucesso!')

if __name__ == '__main__':
    while True:
        rodar_etl()
        time.sleep(10)