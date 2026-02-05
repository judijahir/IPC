import streamlit as st

# --- Interfície Streamlit ---
#st.title("📚 Projecte Final")
st.set_page_config(page_title="Conclusions", page_icon="📈")
#-----------------------------------------------------------------------------------



#---------------------------------------------------------------------------------------------NOW
st.title("📊 Conclusions")

tab_ipc, tab_salari, tab_comp = st.tabs(["📈 IPC", "💶 Salaris", "📊 Comparatiu"])

with tab_ipc:
    #st.subheader("Conclusions sobre l'IPC")
    st.markdown("""
## Conclusions principals de l'IPC (cost de la vida)
L'element clau per entendre les dades és que **l'any 2021 actua com a any base (100)**, ja que és el punt on totes les categories convergeixen abans de tornar a separar-se.

### **1. La gran excepció: Les Comunicacions 📉**
És, amb diferència, el comportament més sorprenent del gràfic. Mentre que gairebé tot puja de preu, les Comunicacions han fet el camí invers:
- L'any 2002 tenien un índex superior a 120 (eren proporcionalment molt cares).
- Han anat baixant de preu de forma constant fins a estabilitzar-se prop del 100.

Això reflecteix com la tecnologia i la competència en telefonia/internet han abaratit aquest servei malgrat la inflació general.

---

### **2. L'acceleració post-pandèmia (2021–2025) 🚀**
Entre 2015 i 2020 les barres creixen lentament i de manera molt ajustada. Però a partir del 2021:
- S'observa un salt brusc en pràcticament totes les categories.
- Coincideix amb el període d'inflació global (energia, subministraments, conflictes bèl·lics).

---

### **3. Aliments i Restauració: els més afectats recentment 🍎🍴**
En els últims anys (2023–2025), algunes categories destaquen clarament:
- **Aliments i begudes no alcohòliques**: creixement molt vertical.
- **Hotels, cafès i restaurants**: també situats a la part alta.

El consum bàsic i el sector serveis han estat els principals motors de la inflació recent.

---

### **4. Estabilitat relativa en el passat**
Durant la dècada del 2010 (2013–2019):
- Les barres es mantenen molt estables.
- Indica una inflació baixa o controlada abans de la volatilitat actual.

---

## 🧭 Resum visual final
El gràfic mostra que **el 2024–2025 és el punt més alt de preus** de tota la sèrie històrica, excepte en tecnologia i comunicacions, que són l’únic àmbit que avui ens costa menys que el 2002.

""")



#-------------------------------------------------------------------------------------------------------------------------------
with tab_salari:
    #st.subheader("Conclusions sobre el salari")
    st.markdown("""

## Claus per entendre l'evolució dels salaris (2019–2023)
Les dades mostren el complement perfecte per al que hem analitzat abans.  
Si l'IPC ens indica com s'han encarit les coses, aquest gràfic ens mostra **com han evolucionat els salaris per fer-hi front**.


### **1. La "fractura" dels 25 anys 🧗**
El primer que destaca és la distància enorme entre la franja més jove i la resta:
- **Menys de 25 anys**: tot i que han passat d’uns 13.000 € a 15.600 €, continuen cobrant pràcticament la meitat del que perceben els majors de 55 anys.
- **Efecte SMI**: entre 2021 i 2023 la línia taronja puja més ràpid, coincidint amb les pujades del Salari Mínim Interprofessional, que afecten sobretot els contractes d’entrada.

---

### **2. L'antiguitat és un grau (i un sou) 📈**
La jerarquia salarial és molt clara: **com més edat, més salari**.
- Les franges de **45–54 anys** i **55+** competeixen pel primer lloc.
- El 2023, els més veterans superen els **33.000 € anuals**, reflectint experiència, estabilitat i càrrecs de responsabilitat.

---

### **3. El salari mitjà, estirat pels extrems ⚖️**
La línia del salari mitjà (blau fosc) actua com a termòmetre general:
- El 2019 estava al voltant dels **26.000 €** i el 2023 ja frega els **30.000 €**.
- El salari mitjà queda **per sota de totes les franges a partir dels 35 anys**, cosa que indica que la precarietat juvenil estira la mitjana cap avall.

---

### **4. Salaris vs. IPC 🤔**
Comparant aquest gràfic amb el de l’IPC:
- **Salaris**: han pujat de manera constant (aprox. +15% des del 2019).
- **IPC**: va accelerar fortament a partir del 2021.
- **Conclusió**: encara que els salaris pugin, si els preus ho fan més ràpid, el **poder adquisitiu real es redueix**, sobretot en franges que no han vist increments significatius.

---

## 📌 Una dada curiosa
Entre **2020 i 2021**, mentre moltes franges es van estancar per la pandèmia, els salaris dels més joves pràcticament no es van moure.

---

## 📈 Increment percentual per franges (2019–2023)

D’acord amb les dades del segon gràfic:

- **Els joves són els que més pugen en percentatge**:  
  Les franges de *menys de 25* i *25–34 anys* creixen gairebé un **20%**.
  
- **Efecte SMI**:  
  Aquest increment coincideix amb les pujades del salari mínim, que han impulsat els sous més baixos.

- **Els sèniors guanyen més en valor absolut**:  
  Tot i créixer “només” un **16,3%**, han guanyat uns **4.700 €** anuals, mentre que els joves només uns **2.600 €**.

- **Comparació amb l’IPC**:  
  Tot i increments del 15–20%, gran part d’aquest augment només ha servit per **no perdre poder adquisitiu** davant la pujada de preus (aliments, energia, habitatge).

""")

    
#--------------------------------------------------------------------------------------------------------------------------------------------
with tab_comp:
    st.markdown("""
## 📈 Conclusions de la comparació de l'IPC i salari

- **L’IPC (línia vermella)** mostra una pujada gairebé contínua des del 2003 fins al 2023. Hi ha petites oscil·lacions, però la tendència és clarament ascendent.
- **El salari mitjà (línia blava)** també creix, però ho fa molt més lentament i amb períodes de pràctica estancada.

Això ja apunta a una idea central: **els preus pugen més i més ràpid que els salaris**.

---

## 🔍 Moments destacats

### **1. 2008–2013: crisi i postcrisi**
- L’IPC continua pujant, tot i que amb alguna frenada.
- Els salaris pràcticament s’estanquen.

Això reflecteix el que sabem d’aquells anys: **pèrdua de poder adquisitiu**.

### **2. 2014–2019: recuperació moderada**
- L’IPC creix de manera suau.
- Els salaris també pugen, però sense recuperar el terreny perdut.

És un període de “recuperació”, però no per a tothom.

### **3. 2020–2023: pandèmia i inflació**
- L’IPC fa un salt molt notable, especialment a partir del 2021.
- Els salaris pugen, però molt menys que els preus.

Aquest és el punt on la bretxa es fa més evident: **la inflació s’accelera i els salaris no la segueixen**.

## 💡 Conclusió clara
El gràfic mostra una realitat contundent:
els salaris no han crescut al mateix ritme que el cost de la vida.
Això implica una pèrdua sostinguda de poder adquisitiu al llarg de 20 anys, especialment marcada en l’última etapa inflacionària.
    """)