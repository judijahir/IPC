import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.io as pio
import plotly.graph_objects as go
# --- Interfície Streamlit ---

st.set_page_config(page_title="Anàlisi descriptiu", page_icon="📈")
# Dades

pio.templates.default = "seaborn"

# Cargar datos
df= pd.read_csv('./dat/work/consolidat.csv', sep=";", decimal=",")


# Crear pestañas
tab_ipc, tab_salarios, tab_comp = st.tabs(["📈 IPC", "💶 Salaris", "📊 Comparatiu"])

# ============================
# 📈 Pestaña IPC
# ============================
# Carregar dades
with tab_ipc:
    df_ipc = pd.read_csv('./dat/work/idescat-ipc.csv', sep=";", decimal=",")

    # Eliminar columna 'status' si existeix
    if "status" in df_ipc.columns:
        df_ipc = df_ipc.drop(columns=["status"])

    st.subheader("IPC anual per categoria")

    # Selector interactiu de categoria
    categories = df_ipc["nom_categ"].unique()
    categoria_seleccionada = st.multiselect(
        "Selecciona una o més categories:",
        options=categories,
        default=[]  # per defecte totes visibles
    )

    # Filtrar segons selecció
    df_filtrat = df_ipc[df_ipc["nom_categ"].isin(categoria_seleccionada)]

    # Gràfic de barres interactiu
    fig = px.bar(
        df_filtrat,
        x="anyy",
        y="ipc",
        color="nom_categ",
        labels={"anyy": "Any", "ipc": "IPC", "nom_categ": "Categoria"},
        title="IPC anual per categoria",
        barmode="group"
    )

    st.plotly_chart(fig, use_container_width=True)


# ============================
# 💶 Pestanya salaris
# ============================
with tab_salarios:
    
    # Cargar datos
    df_sou = pd.read_csv('./dat/work/idescat-salari.csv', sep=";", decimal=",")

    # Asegurar que 'salari' es numérico
    df_sou["salari"] = pd.to_numeric(df_sou["salari"], errors="coerce")

    # Eliminar columna 'status' si existe
    if "status" in df_sou.columns:
        df_sou = df_sou.drop(columns=["status"])

    # Agrupar por año para evitar duplicados
    df_anys = df_sou.groupby("anyy", as_index=False)["salari"].mean()

    # Filtrar últimos 5 años reales
    df_filtrat = df_anys.tail(5)

    st.subheader("Evolució del salari (últims 5 anys)")

    # Gráfico de barras verticales
    fig_sal = px.bar(
        df_filtrat,
        x="anyy",
        y="salari",
        color="anyy",
        title="Salari mitjà (últims 5 anys)"
    )

    # Ajustar rango del eje Y si cal
    fig_sal.update_yaxes(range=[0, 30000], tickvals=[0, 15000, 20000, 25000, 30000])

    st.plotly_chart(fig_sal, use_container_width=True)

    

#--------------------------------------------------------NOW

    st.subheader("Evolució del salari per franja d'edat (últims 5 anys)")

    # Eliminar columna 'status' si existeix
    if "status" in df_sou.columns:
        df_sou = df_sou.drop(columns=["status"])

    # Filtrar els últims 5 anys
    ultims_5 = sorted(df_sou["anyy"].unique())[-5]
    df_sou_5 = df_sou[df_sou["anyy"] >= ultims_5]

    # Gràfic de línia
    fig = px.line(
        df_sou_5,
        x="anyy",
        y="salari",
        color="nom_agrup",
        markers=True,
        labels={"anyy": "Any", "salari": "Salari", "nom_agrup": "Franja d'edat"},
        title="Evolució del salari per franja d'edat"
    )

    st.plotly_chart(fig, use_container_width=True)



# ============================
# 📊 Pestaña Comparativo
# ============================
with tab_comp:
    st.subheader("Comparativa IPC vs Salari")
    df= pd.read_csv('./dat/work/consolidat.csv', sep=";", decimal=",")

    fig_comp = px.scatter(
        df,
        x="ipc",
        y="salari",
        color="anyy",
        size="salari",
        title="Relació entre IPC i Salari"
    )
    st.plotly_chart(fig_comp, use_container_width=True)
    
#--------------------------------------------------

    # Convertir a numèric
    df["ipc"] = pd.to_numeric(df["ipc"], errors="coerce")
    df["salari"] = pd.to_numeric(df["salari"], errors="coerce")

    # Crear figura amb doble eix
    fig_comp = go.Figure()

    # --- Línia IPC (eix Y esquerre) ---
    fig_comp.add_trace(
        go.Scatter(
            x=df["anyy"],
            y=df["ipc"],
            mode="lines+markers",
            name="IPC",
            line=dict(color="red", width=3)
        )
    )

    # --- Línia Salari (eix Y dret) ---
    fig_comp.add_trace(
        go.Scatter(
            x=df["anyy"],
            y=df["salari"],
            mode="lines+markers",
            name="Salari",
            line=dict(color="blue", width=3),
            yaxis="y2"
        )
    )

    # --- Configuració dels eixos ---
    fig_comp.update_layout(
        title="Evolució de l’IPC i el Salari (doble eix)",
        xaxis=dict(title="Any"),

        yaxis=dict(
            title="IPC",
        
            tickfont=dict(color="red")
        ),

        yaxis2=dict(
            title="Salari",
    
            tickfont=dict(color="blue"),
            overlaying="y",
            side="right"
        ),

        legend=dict(x=0.02, y=0.98)
    )

    st.plotly_chart(fig_comp, use_container_width=True)



    



