from pathlib import Path
import pandas as pd

def exportar_resultados(df: pd.DataFrame, output_dir: Path):
    output_dir.mkdir(parents=True, exist_ok=True)

    csv_path = output_dir / "resultados.csv"
    xlsx_path = output_dir / "resultados.xlsx"

    df.to_csv(csv_path, index=False)
    df.to_excel(xlsx_path, index=False)

    return csv_path, xlsx_path