import pandas as pd
from summarizer import resumir_variantes

def test_resumir_variantes_recurrencia():
    df = pd.DataFrame([
        {"sample": "muestra1", "chrom": "9", "pos": 134700000, "ref": "C", "alt": "T"},
        {"sample": "muestra2", "chrom": "9", "pos": 134700000, "ref": "C", "alt": "T"},
        {"sample": "muestra2", "chrom": "9", "pos": 134800000, "ref": "A", "alt": "G"},
    ])

    resumen = resumir_variantes(df)

    fila = resumen[resumen["variant_key"] == "9_134700000_C_T"].iloc[0]
    assert fila["recurrence"] == 2
    assert "muestra1" in fila["samples"]
    assert "muestra2" in fila["samples"]