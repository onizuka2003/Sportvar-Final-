from pathlib import Path
import pandas as pd

def cargar_archivo_variantes(file_path: Path, sample_name: str) -> pd.DataFrame:
    df = pd.read_csv(file_path, sep=None, engine="python")
    df = df.copy()
    df["sample"] = sample_name
    return df

def filtrar_por_region(df: pd.DataFrame, chrom: str, start: int, end: int) -> pd.DataFrame:
    df = df.copy()
    df["chrom"] = df["chrom"].astype(str)
    df["pos"] = df["pos"].astype(int)

    return df[
        (df["chrom"] == str(chrom)) &
        (df["pos"] >= int(start)) &
        (df["pos"] <= int(end))
    ]