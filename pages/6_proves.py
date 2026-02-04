import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

st.subheader("Predicció del salari segons l'any seleccionat")

# Carregar dades
df = pd.read_csv('./dat/consolidat.csv', sep=";", decimal=",")

# Variables del model
X = df[["anyy"]]
y = df["salari"]

# Entrenar model
model = LinearRegression()
model.fit(X, y)

# Selector d'any
anys = list(range(int(df["anyy"].min()), 2031))

any_seleccionat = st.selectbox(
    "Selecciona un any:",
    anys,
    index=anys.index(2026)
)

prediccio = model.predict(np.array([[any_seleccionat]]))[0]

st.write(f"Predicció del salari per a {any_seleccionat}: {prediccio:.2f} €")
