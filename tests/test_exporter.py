import pandas as pd
from pathlib import Path
from exporter import exportar_resultados

def test_exportar_resultados(tmp_path):
    df = pd.DataFrame([
        {"chrom": "9", "pos": 134700000, "ref": "C", "alt": "T", "variant_key": "9_134700000_C_T", "recurrence": 2, "samples": "muestra1, muestra2"}
    ])

    csv_path, xlsx_path = exportar_resultados(df, tmp_path)

    assert Path(csv_path).exists()
    assert Path(xlsx_path).exists()