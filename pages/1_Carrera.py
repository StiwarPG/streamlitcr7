import streamlit as st

st.header('Carrera de Cristiano Ronaldo')

seccion = st.selectbox('Selecciona sección', 
                    ['Logros destacados', 'Fotos icónicas'])

if seccion == 'Logros destacados':
    st.write('Algunos de los logros más importantes de CR7:')
    st.markdown(
        "- Balón de Oro múltiples veces\n"
        "- Récords goleadores en varios clubes y en selección\n"
        "- Títulos nacionales e internacionales con distintos equipos"
    )
elif seccion == 'Fotos icónicas':
    st.write('Galería de imágenes:')
    cols = st.columns(3)
    urls = [
        'https://upload.wikimedia.org/wikipedia/commons/8/8c/Cristiano_Ronaldo_2018.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/Cristiano_Ronaldo_playing_for_Al_Nassr_FC_against_Persepolis%2C_September_2023_%28cropped%29.jpg/800px-Cristiano_Ronaldo_playing_for_Al_Nassr_FC_against_Persepolis%2C_September_2023_%28cropped%29.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/3/3d/C_Ronaldo.jpg'
    ]
    for c, url in zip(cols, urls):
        c.image(url, use_container_width=True)
