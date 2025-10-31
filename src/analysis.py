import pandas as pd

def ventas_sin_igv_por_sede(df: pd.DataFrame):
    return df.groupby("sede")["precio_sin_igv"].sum()

def top_modelos(df: pd.DataFrame, n=5):
    return df["modelo"].value_counts().head(n)

def canales_mas_ventas(df: pd.DataFrame):
    return df.groupby("canal")["precio_sin_igv"].sum()

def clientes_unicos(df: pd.DataFrame):
    return df["cliente"].nunique()

def cantidad_ventas(df: pd.DataFrame):
    return len(df)

def total_ventas(df: pd.DataFrame):
    return {
        "sin_igv": df["precio_sin_igv"].sum(),
        "con_igv": df["precio_con_igv"].sum()
    }