import pandas as pd

def load_data(filepath: str) -> pd.DataFrame:
    """Carga el archivo Excel y devuelve un DataFrame."""
    try:
        df = pd.read_excel(filepath)
        print("Datos cargados correctamente ✅")
        return df
    except FileNotFoundError:
        print("❌ Archivo no encontrado. Verifica la ruta.")
        return pd.DataFrame()
    except Exception as e:
        print(f"⚠️ Error al leer el archivo: {e}")
        return pd.DataFrame()