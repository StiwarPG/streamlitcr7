

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title='CR7 - Proyecto Streamlit', layout='wide')


@st.cache_data
def cargar_datos():
    data = {
        'Temporada': ['2006/07','2007/08','2008/09','2009/10','2010/11','2011/12','2012/13','2013/14','2014/15','2015/16'],
        'Club': ['Man Utd']*3 + ['Real Madrid']*7,
        'Partidos': [49,50,53,54,55,60,55,55,51,46],
        'Goles':    [17,31,33,33,40,46,55,51,61,51],
        'Asistencias':[6,6,9,15,9,12,12,16,22,15]
    }
    df = pd.DataFrame(data)


    tipos_gol = pd.DataFrame({
        'Tipo': ['Cabeza','Penal','Largo alcance','Dentro area','Fuera area'],
        'Cantidad': [60,120,80,400,100]
    })

    return df, tipos_gol

df, tipos_gol = cargar_datos()


PAGINAS = ['Página Principal', 'Carrera', 'Datos y Curiosidades', 'Análisis']
pagina = st.sidebar.radio('Navegación', PAGINAS)


if pagina == 'Página Principal':
    st.title('Cristiano Ronaldo — Proyecto Streamlit (CR7)')
    st.markdown('**Breve descripción:**\n\n    Este proyecto presenta una mini aplicación sobre Cristiano Ronaldo: su carrera, datos curiosos y un análisis visual de sus estadísticas.\n\n    ')

    
    st.image('https://upload.wikimedia.org/wikipedia/commons/8/8c/Cristiano_Ronaldo_2018.jpg', caption='Cristiano Ronaldo', use_container_width=True)

    st.markdown('---')


elif pagina == 'Carrera':
    st.header('Resumen de Carrera')

    seccion = st.selectbox('Selecciona sección', ['Trayectoria por temporadas', 'Logros destacados', 'Fotos icónicas'])

    if seccion == 'Trayectoria por temporadas':
        st.write('A continuación se muestra una tabla con sus temporadas de ejemplo:')
        st.dataframe(df)

    elif seccion == 'Logros destacados':
        st.write('Algunos hitos:')
        st.markdown('- Múltiples Balón de Oro.\n- Récords goleadores en clubes y selección.\n- Títulos en varias ligas europeas.')
        st.write('Puedes personalizar esta sección con más datos históricos o links externos.')

    else:
        st.write('Galería de fotos (usa este espacio para imágenes representativas):')
        cols = st.columns(3)
        for c, url in zip(cols, [
            'https://upload.wikimedia.org/wikipedia/commons/8/8c/Cristiano_Ronaldo_2018.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/1/13/Ronaldo_celebration.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/3/3e/Cristiano_Ronaldo_2014.jpg'
        ]):
            try:
                c.image(url, use_container_width=True)
            except:
                c.write('Imagen no disponible')


elif pagina == 'Datos y Curiosidades':
    st.header('Datos y Curiosidades sobre CR7')

    seccion2 = st.radio('Menú interno', ['Estadísticas rápidas', 'Comparativas', 'Records personales'])

    if seccion2 == 'Estadísticas rápidas':
        total_goles = df['Goles'].sum()
        total_asist = df['Asistencias'].sum()
        st.metric('Goles (muestra 10 temporadas)', total_goles)
        st.metric('Asistencias (muestra 10 temporadas)', total_asist)
        st.write('Tabla resumen:')
        st.table(df[['Temporada','Club','Partidos','Goles']])

    elif seccion2 == 'Comparativas':
        st.write('Aquí podrías comparar a CR7 con otros jugadores o temporadas. Ejemplo simple: goles por temporada (gráfico).')
        fig, ax = plt.subplots()
        ax.bar(df['Temporada'], df['Goles'])
        ax.set_title('Goles por Temporada (muestra)')
        ax.set_ylabel('Goles')
        plt.xticks(rotation=45)
        st.pyplot(fig)

    else:
        st.write('Records personales y curiosidades:')
        st.markdown('- Máximo de goles en una temporada (muestra)\n- Récord de penales convertidos (muestra)\n- Jugador más físicamente preparado: rutina de entrenamiento famosa')


elif pagina == 'Análisis':
    st.header('Página de Análisis')
    st.write('En esta sección mostramos una tabla de datos y varios gráficos que ayudan a interpretar el rendimiento.')

    
    st.subheader('Tabla de datos')
    st.dataframe(df)

    
    st.subheader('Goles por Temporada (Gráfico de Barras)')
    fig1, ax1 = plt.subplots()
    ax1.bar(df['Temporada'], df['Goles'])
    ax1.set_xlabel('Temporada')
    ax1.set_ylabel('Goles')
    ax1.set_title('Goles por Temporada')
    plt.xticks(rotation=45)
    st.pyplot(fig1)

    
    st.subheader('Goles Acumulados (Gráfico de Línea)')
    df['Goles_acum'] = df['Goles'].cumsum()
    fig2, ax2 = plt.subplots()
    ax2.plot(df['Temporada'], df['Goles_acum'], marker='o')
    ax2.set_xlabel('Temporada')
    ax2.set_ylabel('Goles acumulados')
    ax2.set_title('Evolución de Goles Acumulados')
    plt.xticks(rotation=45)
    st.pyplot(fig2)

    
    st.subheader('Goles vs Partidos (Dispersión)')
    fig3, ax3 = plt.subplots()
    ax3.scatter(df['Partidos'], df['Goles'], s=80)
    for i, txt in enumerate(df['Temporada']):
        ax3.annotate(txt, (df['Partidos'].iat[i], df['Goles'].iat[i]))
    ax3.set_xlabel('Partidos')
    ax3.set_ylabel('Goles')
    ax3.set_title('Relación Partidos - Goles')
    st.pyplot(fig3)

    
    st.subheader('Distribución por tipo de gol (Circular)')
    fig4, ax4 = plt.subplots()
    ax4.pie(tipos_gol['Cantidad'], labels=tipos_gol['Tipo'], autopct='%1.1f%%', startangle=140)
    ax4.axis('equal')
    st.pyplot(fig4)

    
    



