from src.data_loader import load_data
from src.analysis import (
    ventas_sin_igv_por_sede,
    top_modelos,
    canales_mas_ventas,
    clientes_unicos,
    cantidad_ventas,
    total_ventas
)
from src.visuals import (
    grafico_ventas_por_sede,
    grafico_top_modelos,
    grafico_canales,
    grafico_segmento_clientes,
    dashboard_resumen
)
from src.report_sender import send_whatsapp_message

# ⚠️ Configura tus credenciales de Twilio aquí
ACCOUNT_SID = "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
AUTH_TOKEN = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
TO_NUMBER = "whatsapp:+58XXXXXXXXXX"  # tu número personal registrado en el sandbox

if __name__ == "__main__":
    # 1. Cargar datos
    df = load_data("data/Ventas Fundamentos.xlsx")
    print("Datos cargados correctamente ✅")

    # 2. Análisis
    print("Ventas sin IGV por sede:\n", ventas_sin_igv_por_sede(df))
    print("\nTop 5 modelos:\n", top_modelos(df))
    print("\nCanales con más ventas:\n", canales_mas_ventas(df))
    print("\nClientes únicos:", clientes_unicos(df))
    print("Cantidad de ventas:", cantidad_ventas(df))
    print("Totales:", total_ventas(df))

    # 3. Visualizaciones
    grafico_ventas_por_sede(df)
    grafico_top_modelos(df)
    grafico_canales(df)
    grafico_segmento_clientes(df)
    dashboard_resumen(df)
    print("✅ Gráficos generados en 'output/'")

    # 4. Enviar reporte por WhatsApp
    body = (
        "📊 *Reporte de Ventas*\n\n"
        f"- Clientes únicos: {clientes_unicos(df)}\n"
        f"- Cantidad de ventas: {cantidad_ventas(df)}\n"
        f"- Total sin IGV: {total_ventas(df)['sin_igv']}\n"
        f"- Total con IGV: {total_ventas(df)['con_igv']}\n"
    )

    # ⚠️ IMPORTANTE: Twilio solo acepta imágenes desde URLs públicas
    # Ejemplo con imágenes subidas a GitHub (reemplaza con tus enlaces reales)
    media_urls = [
        # "https://raw.githubusercontent.com/Pecuca/proyecto-rpa/main/output/ventas_por_sede.png",
        # "https://raw.githubusercontent.com/Pecuca/proyecto-rpa/main/output/top_modelos.png",
        # "https://raw.githubusercontent.com/Pecuca/proyecto-rpa/main/output/canales.png",
        # "https://raw.githubusercontent.com/Pecuca/proyecto-rpa/main/output/segmento_clientes.png",
        # "https://raw.githubusercontent.com/Pecuca/proyecto-rpa/main/output/dashboard.png"
    ]

    send_whatsapp_message(ACCOUNT_SID, AUTH_TOKEN, TO_NUMBER, body, media_urls)
