import streamlit as st

st.set_page_config(layout="wide")

notas = ["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"]
defaults = ["E","B","G","D","A","E","B","G","D","A","E"]
patrones = {
    "mayor":[2,2,1,2,2,2,1],
    "menor":[2,1,2,2,1,2,2],
    "menor armónica":[2,1,2,2,1,3,1],
    "mayor pentatónica":[2,2,3,2,3],
    "menor pentatónica":[3,2,2,3,2]
}

marcas = [3,5,7,9,12,15,17,19,21]

c1,c2,c3,c4,c5 = st.columns([3,1,2,2,3])

with c2: "**Escala de**"
with c3: nota = st.selectbox("Escala",notas,label_visibility="collapsed")
with c4: tipo = st.selectbox("Tipo",patrones,label_visibility="collapsed")

k = notas.index(nota)

completo = 3*notas

escala = [nota]

for salto in patrones[tipo]:
    k += salto
    escala.append(completo[k])

n = st.number_input("Número de cuerdas",min_value=1,max_value=8,step=1,value=6)

T1,T2 = st.tabs(["[ TRASTES ]","[ NOTAS ]"])

with T1:
    c = list(st.columns([2]+23*[1]))
    for j in range(24):
        with c[j]:
            if j in marcas: f"| **{j}**"
            else: "|"

    for i in range(n):
        c = list(st.columns([2]+23*[1]))
        with c[0]:
            tune = st.selectbox("T"+str(i),notas,notas.index(defaults[i]),label_visibility="collapsed")
            #tune = defaults[i]
            #f"**{tune}**"
        for j in range(1,24):
            with c[j]:
                if completo[notas.index(tune) + j] == nota:
                    "| **██**"
                elif completo[notas.index(tune) + j] in escala:
                    "| **▓▓**"
                else: "| _ _ _"

with T2:
    c = list(st.columns([2]+23*[1]))
    for j in range(24):
        with c[j]:
            if j in marcas: f"| **{j}**"
            else: "|"

    for i in range(n):
        c = list(st.columns([2]+23*[1]))
        with c[0]:
            tune = st.selectbox("N"+str(i),notas,notas.index(defaults[i]),label_visibility="collapsed")
            #tune = defaults[i]
            #f"**{tune}**"
        for j in range(1,24):
            with c[j]:
                if completo[notas.index(tune) + j] in escala:
                    f"**| {completo[notas.index(tune) + j]}**"
                else: "| _ _ _"
