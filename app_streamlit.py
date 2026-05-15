import streamlit as st
from src.weather import buscar_clima, recomendacao_clima

st.set_page_config(
    page_title="Discipline Wellness",
    layout="centered"
)

st.title("Discipline Wellness")

st.subheader(
    "Monitoramento inteligente de hábitos saudáveis"
)

st.write(
    "Aplicação desenvolvida para acompanhamento "
    "de wellness, rotina fitness e disciplina."
)

if st.button("Consultar clima atual"):

    dados = buscar_clima()

    if dados:

        temp = dados["temperatura"]

        st.metric(
            label="Temperatura atual",
            value=f"{temp}°C"
        )

        st.success(
            recomendacao_clima(temp)
        )

    else:
        st.error("Erro ao consultar API.")