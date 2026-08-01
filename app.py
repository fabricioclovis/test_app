import streamlit as st
import pandas as pd

st.title('Hello World')

dados = pd.read_csv('dados.csv')
df = pd.DataFrame(dados)
st.write(dados)

st.bar_chart(df, x = 'vendedor', y = 'vendas')

st.map()

st.image('img.png')