from datetime import datetime, timedelta
import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
import plotly.express as px
import pip

pip.main(['install', 'plotly_express'])
pip.main(["install","openpyxl"])

st.text('Se muestra una comparacion del rendimiento del portafolio vs el IPC')
st.title('Gráfico de Retornos Acumulativos')
st.write('Datos de ejemplo:')
st.write('Retorno acumulado del portafolio optimizado:')
st.write(retorno_acum_portafolio)
st.write('Retorno acumulado del índice IPC:')
st.write(retorno_acum_indice)
