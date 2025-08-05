import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv ('vehicles.csv')

st.header ('Anúncios de vendas de carros📊')
hist_button = st.button ('Criar histograma')

if hist_button: # se o botão for clicado
            # escrever uma mensagem
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
            
            # criar um histograma
    fig = px.histogram(df, x="odometer")
        
            # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)
        

scattered_button = st.button ('Criar gráfico de dispersão')

if scattered_button:
    st.write('Criando um gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros')
    fig = px.scatter(df, x="odometer")
    st.plotly_chart(fig, use_container_width=True)
        


build_histogram = st.checkbox ('Criar um histograma')

if build_histogram:
    st.write('Criando um histograma para a coluna odometer')
    fig = px.histogram(df, x="odometer", y='price')
    st.plotly_chart(fig, use_container_width=True)

build_scatter = st.checkbox ('Criar um gráfico de dispersão')
    
if build_scatter:
    st.write('Criando um gráfico de dispersão para a coluna odometer')
    fig_scattered = px.scatter (df, x= 'odometer', y= 'price')
    st.plotly_chart(fig_scattered, use_container_width=True)

#Decidi deixar as duas opção de gráficos, tanto a de botão como a de opção, para a avaliação do projeto. 