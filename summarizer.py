import pandas as pd

def resumir_variantes(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        return df

    df = df.copy()
    df["variant_key"] = (
        df["chrom"].astype(str) + "_" +
        df["pos"].astype(str) + "_" +
        df["ref"].astype(str) + "_" +
        df["alt"].astype(str)
    )

    resumen = (
        df.groupby(["chrom", "pos", "ref", "alt", "variant_key"], as_index=False)
        .agg(
            recurrence=("sample", "nunique"),
            samples=("sample", lambda x: ", ".join(sorted(set(map(str, x)))))
        )
        .sort_values(["chrom", "pos"])
    )

    return resumen