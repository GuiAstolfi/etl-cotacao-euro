import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import time
import plotly.express as px

# Função para ler os dados do banco
def read_data():
    engine = create_engine('sqlite:///cotacao_euro.db')
    df = pd.read_sql('SELECT * FROM cotacao_euro ORDER BY "data da conversão" DESC', con=engine)
    return df

st.set_page_config(layout= 'wide')
# Título do app
st.title("Cotação do EURO em Tempo Real 💶")

# Atualização manual
if st.button("🔄 Atualizar DashBoard"):
    st.rerun()

# Carregar os dados
df = read_data()

df['valor máximo'] = df['valor máximo'].astype(float)
df['valor mínimo'] = df['valor mínimo'].astype(float)

df.info()
# Mostrar os dados mais recentes
if not df.empty:

    # Mostrar tabela com histórico
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Histórico das Cotações")
        st.dataframe(df[['data da conversão', 'valor máximo', 'valor mínimo', 'comparação anterior']])

    col3, col4 = st.columns(2)
    with col3:
        st.metric("💰 Valor Máximo", f"R$ {df['valor máximo'].max():.2f}")
    with col4:
        st.metric("📉 Valor Mínimo", f"R$ {df['valor mínimo'].min():.2f}")

    with col2:
        st.subheader('Evolução do preço do EURO')
        grafico = px.line(df, x= 'data da conversão', y= 'valor máximo')
        st.plotly_chart(grafico)
else:
    st.warning("Nenhum dado disponível ainda. Aguarde a próxima coleta.")