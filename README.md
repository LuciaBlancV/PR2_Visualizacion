# Práctica 2 Visualización de Datos - Spotify Tracks
![image](https://github.com/LuciaBlancV/PR2_Visualizacion/assets/148953141/60a9d182-178e-41cd-a5a0-4a00d73d4907) 

## Máster Ciencia de Datos (UOC)
## Lucia Blanc Velázquez
Este script en Python proporciona una visualización integral de los datos de canciones de Spotify utilizando diversas bibliotecas como Plotly, Seaborn y Streamlit. El script lee un archivo CSV que contiene información sobre las pistas de Spotify y genera visualizaciones perspicaces para explorar tendencias y patrones dentro del conjunto de datos.


### Spotify 
Spotify transformó para siempre la forma de escuchar música cuando se lanzó en Suecia en 2008. Descubre, gestiona y comparte más de 70 millones de canciones de forma gratuita, o suscríbete a Spotify Premium para acceder a funciones exclusivas como el modo sin conexión, una calidad de sonido mejorada y una experiencia musical sin anuncios. En la actualidad, Spotify es el servicio de streaming de audio más popular del mundo, con 365 millones de usuarios y 165 millones de suscriptores en 178 mercados. Es el mayor generador de ingresos para el negocio de la música en la actualidad.


### Dataset
Un conjunto de datos de canciones de Spotify de distintos géneros y sus características de audio.

*Fuente:* Kaggle

*Autor*: Maharshi Pandya


Variables: 

* artist: Nombre del artista
  
* song: Nombre de la pista.
  
* duration_ms: Duracion de la pista en milisegundos
  
* explicit: La letra o el contenido de una canción o un vídeo musical contienen uno o varios de los criterios que podrían considerarse ofensivos o inadecuados para los niños.
  
* year: Año de publicación de la pista.
  
* popularity: Cuanto más alto es el valor, más popular es la canción.
  
* danceability: La bailabilidad describe lo adecuada que es una pista para bailar basándose en una combinación de elementos musicales como el tempo, la estabilidad del ritmo, la fuerza del compás y la regularidad general. Un valor de 0,0 es el menos bailable y 1,0 el más bailable.
  
* energy: La energía es una medida de 0,0 a 1,0 y representa una medida perceptiva de intensidad y actividad.
  
* key: La tonalidad de la pista. Los números enteros se asignan a tonos utilizando la notación estándar Pitch Class. Por ejemplo, 0 = C, 1 = C♯/D♭, 2 = D, y así sucesivamente. Si no se detectó ninguna clave, el valor es -1.
  
* loudness: La sonoridad global de una pista en decibelios (dB). Los valores de sonoridad se promedian en toda la pista y son útiles para comparar la sonoridad relativa de las pistas. La sonoridad es la cualidad de un sonido que es el principal correlato psicológico de la fuerza física (amplitud). Los valores suelen oscilar entre -60 y 0 db.
  
* mode: El modo indica la modalidad (mayor o menor) de una pista, el tipo de escala del que se deriva su contenido melódico. Mayor se representa con 1 y menor con 0.
  
* speechiness: La locuacidad detecta la presencia de palabras habladas en una pista. Cuanto más exclusivamente hablada sea la grabación (por ejemplo, programa de entrevistas, audiolibro, poesía), más se acercará a 1,0 el valor del atributo. Los valores superiores a 0,66 describen pistas que probablemente estén compuestas en su totalidad por palabras habladas. Los valores entre 0,33 y 0,66 describen pistas que pueden contener tanto música como voz, ya sea en secciones o en capas, incluyendo casos como la música rap. Los valores inferiores a 0,33 representan probablemente música y otras pistas no habladas.
  
* acousticness: Una medida de confianza de 0,0 a 1,0 sobre si la pista es acústica. 1,0 representa una confianza alta en que la pista es acústica.
  
* instrumentalness: Predice si una pista no contiene voces. Los sonidos "ooh" y "aah" se consideran instrumentales en este contexto. Las pistas de rap o spoken word son claramente "vocales". Cuanto más se acerque el valor de instrumental a 1,0, mayor será la probabilidad de que la pista no contenga voces. Los valores superiores a 0,5 representan pistas instrumentales, pero la confianza es mayor a medida que el valor se acerca a 1,0.
  
* liveness: Detecta la presencia de público en la grabación. Los valores de liveness más altos representan una mayor probabilidad de que la pista se haya interpretado en directo. Un valor superior a 0,8 proporciona una gran probabilidad de que la pista sea en directo.
  
* valence: Medida de 0,0 a 1,0 que describe la positividad musical que transmite una pista. Las pistas con valencia alta suenan más positivas (por ejemplo, felices, alegres, eufóricas), mientras que las pistas con valencia baja suenan más negativas (por ejemplo, tristes, deprimidas, enfadadas).
  
* tempo: El tempo global estimado de una pista en pulsaciones por minuto (BPM). En terminología musical, el tempo es la velocidad o el ritmo de una pieza determinada y se deriva directamente de la duración media del compás.
  
* genre: Genero de la pista.




### Visualizaciones

*1. Matriz de Correlación:* Muestra las correlaciones entre columnas numéricas en el conjunto de datos.

*2. Top 20 Artistas Populares:* Gráfico de barras que muestra los 20 artistas más populares según la popularidad de las pistas.

*3. Top 10 Géneros Populares:* Gráfico de barras que ilustra los 10 géneros más populares según la popularidad de las pistas.

*4. Top 10 Canciones en Spotify:* Gráfico de líneas que presenta la popularidad de las 10 canciones principales en Spotify.

*5. Tempo vs. Popularidad:* Gráfico de dispersión que muestra la relación entre el tempo y la popularidad de las pistas.

*6. Energía vs. Bailabilidad:* Gráfico de dispersión que ilustra la relación entre la energía y la bailabilidad de las pistas.

*7. Correlación Energía vs. Volumen:* Gráfico de dispersión que muestra la correlación entre la energía y el volumen.




### Requisitos y Dependencias
Se deben tener instaladas las siguientes bibliotecas de Python:

Dependencias: *pandas*, *numpy*, *matplotlib*, *plotly*, *seaborn*, *streamlit*

Se pueden instalar utilizando el siguiente comando:

```bash
pip install pandas numpy matplotlib plotly seaborn streamlit
```

## Streamlit App
Una vez se hayan instalado las dependencias, para poder ver la visualización, se debe escribir el siguiente código en el terminal: 

```bash
streamlit run Spotify_tracks.py
```

