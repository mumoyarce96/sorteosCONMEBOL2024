# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 18:36:13 2023

@author: Raimundo
"""

import streamlit as st
from sorteoLibertadores import simular, sorteo_a_dataframe
import pandas as pd

st.set_page_config(page_title = "Sorteo Copa Libertadores 2024")
# CSS to inject contained in a string
hide_dataframe_row_index = """
            <style>
            .row_heading.level0 {display:none}
            .blank {display:none}
            </style>
            """

# Inject CSS with Markdown
st.markdown(hide_dataframe_row_index, unsafe_allow_html=True)

st.title('Simulación:')
st.header('Sorteo de la Copa Libertadores 2024')
st.subheader('Equipos por bolillero')
b1 = [
    'Fluminense (Brasil)',
    'Palmeiras (Brasil)',
    'River Plate (Argentina)',
    'Flamengo (Brasil)',
    'Grêmio (Brasil)',
    'Peñarol (Uruguay)',
    'São Paulo (Brasil)',
    'LDU Quito (Ecuador)'
]

b2 = [
    'Atlético Mineiro (Brasil)',
    'Independiente del Valle (Ecuador)',
    'Libertad (Paraguay)',
    'Cerro Porteño (Paraguay)',
    'Estudiantes (Argentina)',
    'Barcelona (Ecuador)',
    'Bolívar (Bolivia)',
    'Junior (Colombia)'
]

b3 = equipos = [
    'San Lorenzo (Argentina)',
    'The Strongest (Bolivia)',
    'Universitario (Perú)',
    'Deportivo Táchira (Venezuela)',
    'Rosario Central (Argentina)',
    'Alianza Lima (Perú)',
    'Millonarios (Colombia)',
    'Talleres (Argentina)'
]

b4 = [
    'Caracas (Venezuela)',
    'Liverpool (Uruguay)',
    'Huachipato (Chile)',
    'Cobresal (Chile)',
    'Botafogo (Brasil)*',
    'Palestino (Chile)*',
    'Nacional (Uruguay)*',
    'SColo Colo (Chile)*'
]


dict_bolilleros = {'Bolillero 1': b1,
                   'Bolillero 2': b2,
                   'Bolillero 3': b3,
                   'Bolillero 4': b4}
df_bolilleros = pd.DataFrame(dict_bolilleros)
st.table(df_bolilleros)
st.caption('*Equipo clasificado desde la Fase Previa')

    

if st.button('Sortear grupos'):
    st.subheader('Grupos simulados')
    df_sorteo = sorteo_a_dataframe(simular({'Fluminense': 'A'}))
    st.table(df_sorteo[['A', 'B', 'C', 'D']])
    st.table(df_sorteo[['E', 'F', 'G', 'H']])
