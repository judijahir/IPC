import streamlit as st
import pandas as pd

def carregar_arxiu(path: str) -> pd.DataFrame:
    """Carrega l'arxiu des d'un CSV."""
    df =  pd.read_csv(path, sep =";", decimal=",")
    return df

def mostrar_dades(tipus, df: pd.DataFrame):
    st.subheader("Dades "+ tipus)
    st.dataframe(df)

#---------------------------------

st.title("📥 Càrrega de dades")

st.write("Carrega els fitxers idescat CSV per fer l'anàlisi")
st.page_link("https://www.idescat.cat/", label="descarregats de Idescat", icon="🌎")


# Carrega IPC
ipc_file = st.file_uploader("Carrega el fitxer aec-ipc", type="csv")
if ipc_file:
    st.session_state["df_ipc"] = carregar_arxiu(ipc_file)
    st.success("df_ipc carregat correctament!")
    mostrar_dades("ipc", st.session_state["df_ipc"].head(3))

# Carrega SOU
sou_file = st.file_uploader("Carrega el fitxer basics-salary.csv", type="csv")
if sou_file:
    st.session_state["df_sou"] = carregar_arxiu(sou_file)
    st.success("df_sou carregat correctament!")
    mostrar_dades("sou", st.session_state["df_sou"].head(3))
    
# Carrega Indicadors de benestar i progrés social
bene_file = st.file_uploader("Carrega el fitxer idescat-indbps.csv", type="csv")
if bene_file:
    st.session_state["df_bene"] = carregar_arxiu(bene_file)
    st.success("df_bene carregat correctament!")
    mostrar_dades("Benestar", st.session_state["df_bene"].head(3))

if st.button("Consolidar i netejar"):
    if "df_ipc" in st.session_state:
        df_ipc = st.session_state["df_ipc"]
        df_ipc.to_csv("./dat/work/idescat-ipc.csv", index=False, sep =";", decimal=",")
        if "df_sou" in st.session_state:
            df_sou = st.session_state["df_sou"]
            df_sou.to_csv("./dat/work/idescat-salari.csv", index=False, sep =";", decimal=",")
            #
            # Prepara el consolidat per any i seleccionant el global
            df_ipc_filt = df_ipc[df_ipc.id_categ==1][['anyy', 'ipc']]
            df_sou_filt = df_sou[df_sou.id_agrup==1][['anyy', 'salari']]
            df_union = pd.merge(df_ipc_filt, df_sou_filt, on="anyy",
                                how="inner")
            st.session_state["df_union"] = df_union
            df_union.to_csv("./dat/work/consolidat.csv", index=False, sep =";", decimal=",")
            #
            # Afegeix Indicadors de Benestar
            if "df_bene" in st.session_state:
                df_bene = st.session_state["df_bene"]
                df_union = pd.merge(df_union, df_bene[['anyy','RendaLlar','TxAturJoves']],
                                    on="anyy", how="left")
                st.session_state["df_union"] = df_union
                df_union.to_csv("./dat/work/consolidat.csv",  index=False, sep =";", decimal=",")
            else:
                st.write("Consolido sense dades de benestar")
        else:
           st.write("Cal carregar dades de sous")
    else:
        st.write("Cale carregar dades de ipc") 
        
    st.write("Dades consolidades !!")
else:
    st.write("Pendent de consolidar...")

#------------------------------------------------------------------Texto

st.write("Aquí es carreguen els fitxers, quan l'usuari prem 'consolidar i netejar', el programa guarda els fitxers de l'IPC i salari en una carpeta local.")









