from pathlib import Path
import pandas as pd

from gene_service import obtener_region_gen
from extractor import cargar_archivo_variantes, filtrar_por_region
from summarizer import resumir_variantes
from exporter import exportar_resultados
from config import OUTPUTS_DIR

def ejecutar_analisis(gene: str, files: list[Path]):
    region = obtener_region_gen(gene)
    if not region:
        raise ValueError(f"No se encontró el gen: {gene}")

    todos = []
    for file_path in files:
        sample_name = file_path.stem
        df = cargar_archivo_variantes(file_path, sample_name)
        filtrado = filtrar_por_region(df, region["chrom"], region["start"], region["end"])
        if not filtrado.empty:
            todos.append(filtrado)

    if not todos:
        return pd.DataFrame(), None, None

    unidos = pd.concat(todos, ignore_index=True)
    resumen = resumir_variantes(unidos)
    csv_path, xlsx_path = exportar_resultados(resumen, OUTPUTS_DIR)

    return resumen, csv_path, xlsx_path