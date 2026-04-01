import streamlit as st
from config import SAMPLE_DATA_DIR
from analysis_service import ejecutar_analisis

st.set_page_config(page_title="SportVar", layout="wide")

st.title("SportVar")
st.write("Análisis básico de variantes por gen")

gene = st.text_input("Ingresa un gen", value="COL5A1")

archivos = list(SAMPLE_DATA_DIR.glob("*.csv")) + list(SAMPLE_DATA_DIR.glob("*.tsv"))

st.write("Archivos detectados en sample_data:")
for archivo in archivos:
    st.write(f"- {archivo.name}")

if st.button("Ejecutar análisis"):
    try:
        resumen, csv_path, xlsx_path = ejecutar_analisis(gene, archivos)

        if resumen.empty:
            st.warning("No se encontraron variantes para esa región.")
        else:
            st.success("Análisis completado")
            st.dataframe(resumen, use_container_width=True)
            st.write(f"CSV generado: {csv_path}")
            st.write(f"XLSX generado: {xlsx_path}")

    except Exception as e:
        st.error(f"Error: {e}")