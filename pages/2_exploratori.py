import streamlit as st
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px


# FUNCIONES

def mostrar_ipc():
    
    # Cargar datos
    df = pd.read_csv('./dat/work/consolidat.csv', sep=";", decimal=",")
    df_ipc = pd.read_csv('./dat/work/idescat-ipc.csv', sep=";", decimal=",")
    
    # Eliminar columna 'status' si existe
    if "status" in df_ipc.columns:
        df_ipc = df_ipc.drop(columns=["status"])

    # Mostrar
    st.header("Anàlisi de l'IPC")

    st.dataframe(df.head(3), hide_index=True)

    st.write("Valors estadístics de la mostra (IPC)")
    st.write(df['ipc'].describe())

    # --- Histograma IPC ---
    st.subheader("Histograma de l'IPC")

    fig, ax = plt.subplots()
    ax.hist(
        df.ipc,
        bins=15,
        edgecolor='black',
        color='#4C72B0'
    )
    ax.set_xlabel("IPC")
    ax.set_ylabel("Freqüència")
    ax.set_title("Distribució de l'IPC")

    st.pyplot(fig)

    # --- Mitjana IPC per any ---
    df_mitjanes_ipc = df.groupby("anyy")['ipc'].mean().reset_index()

    st.write("Mitjana de l'índex general per any:")
    st.dataframe(df_mitjanes_ipc, hide_index=True)

    # --- Boxplot IPC ---
    st.subheader("Box Plot de la mitjana de l'IPC per any")

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.boxplot(
        df_mitjanes_ipc['ipc'],
        vert=True,
        patch_artist=True,
        boxprops=dict(facecolor='#4C72B0', color='black'),
        medianprops=dict(color='yellow', linewidth=2),
        whiskerprops=dict(color='black'),
        capprops=dict(color='black'),
        flierprops=dict(marker='o', markerfacecolor='red', markersize=6)
    )
    ax.set_title("Distribució de la mitjana anual de l'IPC")
    ax.set_ylabel("Índex general (IPC)")

    st.pyplot(fig)
    
    st.subheader("Evolució de l'IPC des del 2020")
   



    # Filtrar els últims 6 anys
    ultims_6 = sorted(df_ipc["anyy"].unique())[-6]
    df_filtrat = df_ipc[df_ipc["anyy"] >= ultims_6]

    # Boxplot IPC per als últims 5 anys
    fig = px.box(
        df_filtrat,
        x="anyy",
        y="ipc",
        color="anyy",
        labels={
            "anyy": "Any",
            "ipc": "IPC"
        },
        title="Distribució de l'IPC per any de totes les categoria a partir del 2020"
    )

    st.plotly_chart(fig, use_container_width=True)
#---------------------------------------------------------------Text
    st.write("Carrega les dades i llegeix el fitxer consolidat (IPC + salari)")
    st.write("Mostra de gràfics: Histograma; distribució de valors de l'IPC. Boxplot; mostra la mitjana anual per veure la variabilitat d'aquestes. Boxplot per any amb Plotly; per analitzar la distribució de l'IPC en els anys més recents.")

def mostrar_salari():
    
    # Cargar datos
    df = pd.read_csv('./dat/work/consolidat.csv', sep=";", decimal=",")
    df_sal = pd.read_csv('./dat/work/idescat-salari.csv', sep=";", decimal=",")
    
    st.header("Anàlisi del Salari")

    st.dataframe(df.head(3), hide_index=True)

    st.write("Valors estadístics de la mostra (Salari)")
    st.write(df['salari'].describe())

    # --- Histograma Salari ---
    st.subheader("Histograma del salari")

    fig, ax = plt.subplots()
    ax.hist(
        df.salari,
        bins=15,
        edgecolor='black',
        color='#55A868'
    )
    ax.set_xlabel("Salari")
    ax.set_ylabel("Freqüència")
    ax.set_title("Distribució del salari")

    st.pyplot(fig)

    # --- Mitjana salari per any ---
    df_mitjanes_salari = df.groupby("anyy")['salari'].mean().reset_index()

    st.write("Mitjana del salari per any:")
    st.dataframe(df_mitjanes_salari, hide_index=True)

    # --- Boxplot salari ---
    st.subheader("Box Plot de la mitjana del salari per any")

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.boxplot(
        df_mitjanes_salari['salari'],
        vert=True,
        patch_artist=True,
        boxprops=dict(facecolor='#55A868', color='black'),
        medianprops=dict(color='yellow', linewidth=2),
        whiskerprops=dict(color='black'),
        capprops=dict(color='black'),
        flierprops=dict(marker='o', markerfacecolor='red', markersize=6)
    )
    ax.set_title("Distribució de la mitjana anual del salari")
    ax.set_ylabel("Salari")

    st.pyplot(fig)
#--------------------

    st.subheader("Evolució del salari (últims 5 anys)")


    # Filtrar els últims 5 anys
    ultims_5 = sorted(df_sal["anyy"].unique())[-5]
    df_filtrat = df_sal[df_sal["anyy"] >= ultims_5]

    # Boxplot del salari per als últims 5 anys
    fig = px.box(
        df_filtrat,
        x="anyy",
        y="salari",
        color="anyy",
        labels={
            "anyy": "Any",
            "salari": "Salari"
        },
        title="Distribució del salari per any (últims 5 anys)"
    )

    st.plotly_chart(fig, use_container_width=True)

#---------------------------------------------------------------Text
    st.write("Aquest Boxplot calcula la mitjana anual del salari agrupant les dades per any. Es genera els gràfics que permeten identificar:  ")
    st.write("""La mediana del salari mitjà anual.

La variabilitat entre anys.

La presència de possibles valors atípics (outliers).

L’amplitud interquartílica, que indica la dispersió de les mitjanes.""")
    
#_________________________________________________________ INICIO DEL PROGRAMA

# --- Interfície Streamlit ---
st.title("📚 Projecte Final")
st.set_page_config(page_title="Anàlisi exploratòri", page_icon="📈")

# --- Crear pestanyes ---
tab_ipc, tab_salari = st.tabs(["📊 IPC", "💶 Salari"])

# ============================================================
#                           TAB IPC
# ============================================================
with tab_ipc:
    mostrar_ipc()

# ============================================================
#                        TAB SALARI
# ============================================================
with tab_salari:

    mostrar_salari()
    


 

