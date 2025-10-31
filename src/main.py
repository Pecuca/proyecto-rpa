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
    grafico_segmento_clientes
)
from src.report_sender import send_whatsapp_message

# ⚠️ Configura tus credenciales de Twilio aquí
ACCOUNT_SID = "TU_ACCOUNT_SID"
AUTH_TOKEN = "TU_AUTH_TOKEN"
TO_NUMBER = "whatsapp:+58XXXXXXXX"  # tu número de WhatsApp

if __name__ == "__main__":
    # 1. Cargar datos
    df = load_data("data/Ventas Fundamentos.xlsx")

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
    print("✅ Gráficos generados en 'output/'")

    # 4. Enviar reporte por WhatsApp
    body = (
        "📊 *Reporte de Ventas*\n\n"
        f"- Clientes únicos: {clientes_unicos(df)}\n"
        f"- Cantidad de ventas: {cantidad_ventas(df)}\n"
        f"- Total sin IGV: {total_ventas(df)['sin_igv']}\n"
        f"- Total con IGV: {total_ventas(df)['con_igv']}\n"
    )

    # Aquí deberías poner URLs públicas de los gráficos si quieres enviarlos
    media_urls = [
        # "https://mi-servidor.com/ventas_por_sede.png",
        # "https://mi-servidor.com/top_modelos.png"
    ]

    send_whatsapp_message(ACCOUNT_SID, AUTH_TOKEN, TO_NUMBER, body, media_urls)