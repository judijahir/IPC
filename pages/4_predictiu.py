import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

st.title("📈 Models de regressió: Any i IPC")

# --- Càrrega del CSV ---
df = pd.read_csv('./dat/work/consolidat.csv', sep=";", decimal=",")
df["anyy"] = df["anyy"].astype(int)

# Crear pestanyes
tab1, tab2 = st.tabs(["📅 Regressió ANY → SALARI", "📊 Regressió IPC → SALARI"])

# ============================
# 1️⃣ PESTANYA 1: ANY → SALARI
# ============================
with tab1:
    st.header("📅 Regressió lineal: Any → Salari")

    # --- Model ANY → SALARI ---
    X_any = df[["anyy"]] = df["anyy"].astype(int)
    y_salari = df["salari"]

    model_any = LinearRegression()
    model_any.fit(X_any, y_salari)

    y_pred_any = model_any.predict(X_any)

    # --- Selectbox per predir salari futur ---
    anys = list(range(2025, 2031))

    any_seleccionat = st.selectbox(
        "Selecciona un any per predir el salari:",
        anys,
        index=anys.index(2026)
    )

    prediccio = model_any.predict(np.array([[any_seleccionat]]))[0]

    st.metric(
        f"Predicció del salari per a {any_seleccionat}",
        round(prediccio, 2),
        border=True
    )

    # --- Gràfic ---
    fig1, ax1 = plt.subplots()
    ax1.scatter(df["anyy"], df["salari"], color="red", label="Dades reals")
    ax1.plot(df["anyy"], y_pred_any, color="blue", label="Regressió lineal")
    ax1.set_xlabel("Any")
    ax1.set_ylabel("Salari (€)")
    ax1.set_title("Regressió lineal: Any → Salari")
    ax1.legend()
    ax1.grid(True)

    st.pyplot(fig1)

    # --- Paràmetres del model ---
    st.write(f"**Coeficient (pendient):** {model_any.coef_[0]:.4f}")
    st.write(f"**Intercept:** {model_any.intercept_:.4f}")

    st.info("""
    Aquesta regressió mostra com evoluciona el salari amb el pas del temps.
    La recta representa la tendència general: si puja, els salaris tendeixen a créixer amb els anys.
    També pots seleccionar un any futur per obtenir una predicció del salari.
    """)


# ============================
# 2️⃣ PESTANYA 2: IPC → SALARI
# ============================
with tab2:
    st.header("📊 Regressió lineal: IPC → Salari")

    X_ipc = df[["ipc"]]
    y_salari = df["salari"]

    model_ipc = LinearRegression()
    model_ipc.fit(X_ipc, y_salari)

    # Ordenem per IPC per dibuixar la recta correctament
    df_sorted = df.sort_values("ipc")
    y_pred_ipc = model_ipc.predict(df_sorted[["ipc"]])

    # Gràfic
    fig2, ax2 = plt.subplots()
    ax2.scatter(df["ipc"], df["salari"], color="green", label="Dades reals")
    ax2.plot(df_sorted["ipc"], y_pred_ipc, color="black", label="Regressió lineal")
    ax2.set_xlabel("IPC")
    ax2.set_ylabel("Salari (€)")
    ax2.set_title("Regressió lineal: IPC → Salari")
    ax2.legend()
    ax2.grid(True)

    st.pyplot(fig2)

    st.write(f"**Coeficient (pendient):** {model_ipc.coef_[0]:.4f}")
    st.write(f"**Intercept:** {model_ipc.intercept_:.4f}")

    st.info("""
    Aquesta regressió analitza si existeix relació entre la inflació (IPC) i el salari.
    La recta mostra la tendència: si és positiva, els salaris tendeixen a pujar quan l’IPC augmenta.
    """)




