

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

@st.cache_data
def cargar_cr7_csv():
    df = pd.read_csv('data/cr7_goals.csv')
    return df

df = cargar_cr7_csv()

st.header('Análisis de Datos de Cristiano Ronaldo')


st.subheader('Tabla de datos — muestra del dataset')
st.dataframe(df.head(20))


st.subheader('Goles por temporada (gráfico de barras)')
goles_por_temp = df.groupby('Season')['Goal_no'].count().reset_index()
fig1, ax1 = plt.subplots(figsize=(10,5))
ax1.bar(goles_por_temp['Season'], goles_por_temp['Goal_no'], color='skyblue')
ax1.set_xlabel('Temporada')
ax1.set_ylabel('Número de goles')
ax1.set_title('Goles por Temporada')
plt.xticks(rotation=45)
st.pyplot(fig1)

st.subheader('Tipo de gol — distribución circular')
tipo = df['Type_of_goal'].value_counts().reset_index()
tipo.columns = ['Tipo de Gol', 'Cantidad']
fig2, ax2 = plt.subplots()
ax2.pie(tipo['Cantidad'], labels=tipo['Tipo de Gol'], autopct='%1.1f%%', startangle=140)
ax2.axis('equal')
st.pyplot(fig2)


st.subheader('Comparativa de goles por competencia')
goles_comp = df.groupby('Competition')['Goal_no'].count().reset_index().sort_values(by='Goal_no', ascending=False)
fig3, ax3 = plt.subplots(figsize=(10,5))
ax3.barh(goles_comp['Competition'], goles_comp['Goal_no'], color='salmon')
ax3.set_xlabel('Número de goles')
ax3.set_ylabel('Competencia')
ax3.set_title('Goles por Competencia')
st.pyplot(fig3)


if 'Minute' in df.columns:
    st.subheader('Minuto del gol vs Temporada')
    df_scatter = df.dropna(subset=['Minute'])

    df_scatter['Season_idx'] = pd.Categorical(df_scatter['Season'], ordered=True, categories=sorted(df_scatter['Season'].unique())).codes
    fig4, ax4 = plt.subplots(figsize=(10,5))
    ax4.scatter(df_scatter['Minute'], df_scatter['Season_idx'], alpha=0.6)
    ax4.set_xlabel('Minuto del Gol')
    ax4.set_ylabel('Temporada (índice)')
    ax4.set_title('Minuto de gol vs temporada')
    st.pyplot(fig4)


