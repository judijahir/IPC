import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error



# --- Interfície Streamlit ---
st.title("📚 Projecte Final")
st.set_page_config(page_title="Anàlisi predictiu", page_icon="📈")
# Dades

# --- Càrrega del CSV ---
df = pd.read_csv('./dat/work/consolidat.csv', sep=";", decimal=",")

# Variables del model
X = df[["anyy"]]      # any com a predictor
y = df["salari"]      # salari com a variable dependent

# Entrenar el model
modelo = LinearRegression()
modelo.fit(X, y)
anys = list(range(2025, 2031))

any_seleccionat = st.selectbox(
    "Selecciona un any:",
    anys,
    index=anys.index(2026)
)

prediccio = modelo.predict(np.array([[any_seleccionat]]))[0]

st.metric(f"Predicció del salari per a {any_seleccionat}", round(prediccio, 2), border = True)


# ============================
# 4. Parámetros del modelo
# ============================
pendiente = modelo.coef_[0]
intercepto = modelo.intercept_

st.write(f"Pendiente (coeficiente): {pendiente:.4f}")
st.write(f"Intercepto: {intercepto:.4f}")

# ============================
# 5. Predicciones del modelo
# ============================
y_pred = modelo.predict(X)


# ============================
# 8. Gráfico del modelo
# ============================


fig, ax = plt.subplots()

ax.scatter(df["ipc"], df["salari"], color="red", label="Dades reals")
ax.plot(df["ipc"], y_pred, color="blue", label="Regressió lineal")

ax.set_xlabel("IPC")
ax.set_ylabel("Salari (€)")
ax.set_title("Model de regressió lineal: IPC → Salari")
ax.legend()
ax.grid(True)

st.pyplot(fig)

# ============================
# 8. Predicció de l'IPC
# ============================
y_ipc = df["ipc"].values
modelo_ipc = LinearRegression()
modelo_ipc.fit(X, y_ipc)


pred_ipc = modelo_ipc.predict(np.array([[any_seleccionat]]))[0]

st.metric(f"Predicció de l'IPC per a {any_seleccionat}", round(pred_ipc, 2), border = True)

st.write("""L’objectiu del model és estimar l’evolució futura del salari a partir de la variable temporal any, utilitzant un model de regressió lineal simple. Aquest enfocament permet obtenir una predicció aproximada del salari per a anys futurs i analitzar la tendència general observada en les dades històriques.
L’usuari pot seleccionar un any entre 2025 i 2030. El model calcula la predicció corresponent i la mostra de manera clara.""")



