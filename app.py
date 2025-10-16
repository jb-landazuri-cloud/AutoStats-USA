import streamlit as st
import pandas as pd
import plotly.express as px

df_vehicles_us = pd.read_csv('vehicles_us.csv')

st.header('Estadisticas de Vehículos en EE.UU.')  # Encabezado

# Creación del Botón del histograma
hist_button = st.button('Mostrar Histograma')

if hist_button:  # Si se hace click en el Botón
    # Se muestra este mensaje
    st.write('Histograma de Anuncios de Venta de Coches')

    # Se crea un histograma
    fig = px.histogram(df_vehicles_us, x="odometer",
                       title='Histograma de Vehículos en EE.UU.')

    # Se muestra un Plotly interactivo del histograma
    st.plotly_chart(fig, use_container_width=True)

####################################################################################################################

# Creación del Botón del Diagrama de Dispersión
hist_button = st.button('Mostrar Diagrama de Dispersión')

if hist_button:  # Si se hace click en el Botón
    # Se muestra este mensaje
    st.write('Diagrama de Dispersión de Anuncios de Venta de Coches')

    # Se crea el Diagrama de Dispersión
    fig = px.scatter(df_vehicles_us, x='price', y='odometer',
                     title='Diagrama de Dispersión de Vehículos en EE.UU.')

    # Se muestra un Plotly interactivo del Diagrama de Dispersión
    st.plotly_chart(fig, use_container_width=True)
