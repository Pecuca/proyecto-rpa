import matplotlib.pyplot as plt

def grafico_ventas_por_sede(df):
    df.groupby("sede")["precio_sin_igv"].sum().plot(kind="bar")
    plt.title("Ventas sin IGV por sede")
    plt.ylabel("Monto")
    plt.tight_layout()
    plt.savefig("output/ventas_por_sede.png")
    plt.close()

def grafico_top_modelos(df):
    df["modelo"].value_counts().head(5).plot(kind="barh")
    plt.title("Top 5 modelos más vendidos")
    plt.xlabel("Cantidad")
    plt.tight_layout()
    plt.savefig("output/top_modelos.png")
    plt.close()

def grafico_canales(df):
    df.groupby("canal")["precio_sin_igv"].sum().plot(kind="bar")
    plt.title("Canales con más ventas")
    plt.ylabel("Monto")
    plt.tight_layout()
    plt.savefig("output/canales.png")
    plt.close()

def grafico_segmento_clientes(df):
    df.groupby("segmento")["precio_sin_igv"].sum().plot(kind="pie", autopct="%1.1f%%")
    plt.title("Segmento de clientes por ventas sin IGV")
    plt.ylabel("")
    plt.tight_layout()
    plt.savefig("output/segmento_clientes.png")
    plt.close()

def dashboard_resumen(df):
    fig, axs = plt.subplots(2, 2, figsize=(10, 8))

    # Ventas por sede
    df.groupby("sede")["precio_sin_igv"].sum().plot(kind="bar", ax=axs[0,0], title="Ventas por sede")

    # Top modelos
    df["modelo"].value_counts().head(5).plot(kind="barh", ax=axs[0,1], title="Top 5 modelos")

    # Canales
    df.groupby("canal")["precio_sin_igv"].sum().plot(kind="bar", ax=axs[1,0], title="Canales con más ventas")

    # Segmento clientes
    df.groupby("segmento")["precio_sin_igv"].sum().plot(kind="pie", autopct="%1.1f%%", ax=axs[1,1])
    axs[1,1].set_ylabel("")
    axs[1,1].set_title("Segmento clientes")

    plt.tight_layout()
    plt.savefig("output/dashboard.png")
    plt.close()
