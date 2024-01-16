# Práctica 2 Visualización de Datos - Spotify Tracks
![image](https://github.com/LuciaBlancV/PR2_Visualizacion/assets/148953141/60a9d182-178e-41cd-a5a0-4a00d73d4907) 

## Máster Ciencia de Datos (UOC)
## Lucia Blanc Velázquez
Este script en Python proporciona una visualización integral de los datos de canciones de Spotify utilizando diversas bibliotecas como Plotly, Seaborn y Streamlit. El script lee un archivo CSV que contiene información sobre las pistas de Spotify y genera visualizaciones perspicaces para explorar tendencias y patrones dentro del conjunto de datos.


Spotify transformó para siempre la forma de escuchar música cuando se lanzó en Suecia en 2008. Descubre, gestiona y comparte más de 70 millones de canciones de forma gratuita, o suscríbete a Spotify Premium para acceder a funciones exclusivas como el modo sin conexión, una calidad de sonido mejorada y una experiencia musical sin anuncios. En la actualidad, Spotify es el servicio de streaming de audio más popular del mundo, con 365 millones de usuarios y 165 millones de suscriptores en 178 mercados. Es el mayor generador de ingresos para el negocio de la música en la actualidad.


### Dataset: Spotify Tracks
Un conjunto de datos de canciones de Spotify de distintos géneros y sus características de audio.

*Fuente:* Kaggle

*Autor*: Maharshi Pandya



### Visualizaciones

*Matriz de Correlación:* Muestra las correlaciones entre columnas numéricas en el conjunto de datos.

*Top 20 Artistas Populares:* Gráfico de barras que muestra los 20 artistas más populares según la popularidad de las pistas.

*Top 10 Géneros Populares:* Gráfico de barras que ilustra los 10 géneros más populares según la popularidad de las pistas.

*Top 10 Canciones en Spotify:* Gráfico de líneas que presenta la popularidad de las 10 canciones principales en Spotify.

*Tempo vs. Popularidad:* Gráfico de dispersión que muestra la relación entre el tempo y la popularidad de las pistas.

*Energía vs. Bailabilidad:* Gráfico de dispersión que ilustra la relación entre la energía y la bailabilidad de las pistas.

*Correlación Energía vs. Volumen:* Gráfico de dispersión que muestra la correlación entre la energía y el volumen.




### Requisitos y Dependencias
Se deben tener instaladas las siguientes bibliotecas de Python:

Dependencias:

*pandas*

*numpy*

*matplotlib*

*plotly*

*seaborn*

*streamlit*


Se pueden instalar utilizando el siguiente comando:

```bash
pip install pandas numpy matplotlib plotly seaborn streamlit
```

## Streamlit App
Una vez se hayan instalado las dependencias, para poder ver la visualización, se debe escribir el siguiente código en el terminal: 

```bash
streamlit run nombre_del_script.py
```

