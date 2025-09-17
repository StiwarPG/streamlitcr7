

import streamlit as st
import pandas as pd


@st.cache_data
def cargar_cr7_csv():
    df = pd.read_csv('data/cr7_goals.csv')  
    return df

df = cargar_cr7_csv()

st.header('Datos y Curiosidades de Cristiano Ronaldo')

seccion2 = st.radio('Menú interno', 
                    ['Estadísticas rápidas', 'Comparativas', 'Records personales'])

if seccion2 == 'Estadísticas rápidas':
    st.write('Algunas estadísticas del dataset:')
    
    goles_por_club = df.groupby('Team')['Goal_no'].count().sort_values(ascending=False).reset_index()
    goles_por_club.columns = ['Club','Goles totales']
    st.table(goles_por_club.head(10))
    
elif seccion2 == 'Comparativas':
    st.write('Comparativa de goles por temporada:')
    goles_por_temp = df.groupby('Season')['Goal_no'].count().reset_index()
    st.bar_chart(data=goles_por_temp.set_index('Season'))
    
elif seccion2 == 'Records personales':
    st.write('Algunos records especiales:')
    
    max_goles_temp = df.groupby('Season')['Goal_no'].count().idxmax()
    st.write(f"Temporada con más goles: {max_goles_temp}")
