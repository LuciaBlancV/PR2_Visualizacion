#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 22:24:54 2024

@author: luciablanc
"""


# Importing all the Required Libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from plotly.offline import plot
import seaborn as sns
import datetime as dt
import warnings
import scipy.stats as stats
import streamlit as st


warnings.filterwarnings('ignore')
pd.set_option('display.max_columns',None)




# Lee el archivo CSV
df_spotify = pd.read_csv('/Users/luciablanc/Documents/AAESTUDIOS/UOC_Máster_Data_Science/4t_Semestre/Visualización_datos/PR2/Spotify_tracks.csv')


df_spotify.info()

# Validamos si hay valores nulos
df_spotify.isnull().sum()

# Validamos si hay valores duplicados
df_spotify.duplicated().value_counts()


# Eliminamos los valores duplicados
df_spotify.drop_duplicates(inplace=True)

# Forma del conjunto de datos
df_spotify.shape

# Descripción de los datos
df_spotify.describe()


# Visualizations

imagen_path = "/Users/luciablanc/Downloads/Spotify_logo.png"

# Streamlit App
st.title("Spotify Data Visualization")

# Muestra la imagen en Streamlit
st.image(imagen_path,  use_column_width=True)




# First Row
col1 , col2 = st.columns(2)

# 1. Correlation Matrix
numeric_columns = df_spotify.select_dtypes(include=[np.number]).columns
fig1 = px.imshow(df_spotify[numeric_columns].corr(), text_auto=True, height=400, width=400,
                 color_continuous_scale=px.colors.sequential.Greens, aspect='auto', title='Pairwise Correlations')
col1.plotly_chart(fig1)



# 2. Top 20 Popular Singers
fig2 = px.bar(df_spotify.groupby('artists', as_index=False).sum().sort_values(by='popularity', ascending=False).head(20),
              x='artists', y='popularity', color_discrete_sequence=['lightgreen'], template='plotly_dark',
              text='popularity', title='Top 20 Popular Singers')
col2.plotly_chart(fig2)





# Second row
col3 = st.columns(1)[0]

# 3. Top 5 Popular Genres of Popular Artists
fig3 = px.bar(df_spotify.groupby('track_genre', as_index=False).sum().sort_values(by='popularity', ascending=False).head(10),
              x='track_genre', y='popularity', color_discrete_sequence=['lightgreen'],
              template='plotly_dark', text='popularity', title='Top 10 Popular Genres')

fig3.update_layout(
    xaxis=dict(title='Track Genre'),
    yaxis=dict(title='Popularity'),
)

col3.plotly_chart(fig3)


# Third row
col4 = st.columns(1)[0]

fig4 = px.line(df_spotify.sort_values(by='popularity', ascending=False).head(27), x='track_name', y='popularity',
               hover_data=['artists'], color_discrete_sequence=['green'], markers=True,
               title='Top 10 songs in Spotify')  
fig4.update_layout(
    title=dict(text='Top 10 songs in Spotify'), 
    xaxis=dict(title='Track Name'),
    yaxis=dict(title='Popularity'),
)
col4.plotly_chart(fig4)




# Fourth Row
col5, col6, col7 = st.columns(3)

# 5. Tempo vs. Popularity
fig5 = px.scatter(df_spotify, x='tempo', y='popularity', color='tempo',
                  color_continuous_scale=px.colors.sequential.Greens, template='plotly_dark',
                  title='Tempo Versus Popularity')
fig5.update_layout(
    xaxis=dict(title='Tempo'),
    yaxis=dict(title='Popularity'),
)
col5.plotly_chart(fig5)


# 6. Energy vs. Danceability
fig6 = px.scatter(df_spotify, x='energy', y='danceability', color='danceability',
                  color_continuous_scale=px.colors.sequential.Greens, template='plotly_dark',
                  title='Energy Versus Danceability')
fig6.update_layout(
    xaxis=dict(title='Energy'),
    yaxis=dict(title='Danceability'),
)
col6.plotly_chart(fig6)


# 7. Correlation Energy vs. Loudness
fig7 = px.scatter(df_spotify, x='energy', y='loudness', color_discrete_sequence=['lightgreen'],
                  template='plotly_dark', title='Energy versus Loudness correlation')
fig7.update_layout(
    xaxis=dict(title='TEnergy'),
    yaxis=dict(title='Loudness'),
)
col7.plotly_chart(fig7)

