# 📊 Proyecto RPA de Ventas con WhatsApp

Este proyecto implementa un flujo completo de **automatización de reportes de ventas**:
1. Lectura de datos desde un archivo Excel.
2. Análisis de métricas clave (ventas sin IGV, top modelos, canales, clientes únicos, etc.).
3. Generación de gráficos con Matplotlib.
4. Envío automático del reporte por **WhatsApp** usando Twilio.

---

## 🚀 Requisitos

- Python 3.9+
- Cuenta en [Twilio](https://www.twilio.com/)
- Activación del sandbox de WhatsApp en Twilio

---

## ⚙️ Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tu-usuario/proyecto-rpa.git
   cd proyecto-rpa
   ```

2. Crea y activa un entorno virtual:
   ```bash
   python -m venv venv
   venv\Scripts\activate   # Windows
   source venv/bin/activate # Linux/Mac
   ```

3. Instala dependencias:
   ```bash
   pip install -r requirements.txt
   ```

---

## 📊 Uso

1. Coloca el archivo `Ventas Fundamentos.xlsx` en la carpeta `data/`.
2. Ejecuta el proyecto:
   ```bash
   python -m src.main
   ```
3. Se generarán gráficos en la carpeta `output/`.
4. Si configuraste Twilio, recibirás el reporte en tu WhatsApp.

---

## 📱 Configuración de Twilio

1. Obtén tu `ACCOUNT_SID` y `AUTH_TOKEN` desde el [Dashboard de Twilio](https://www.twilio.com/console).
2. Activa el sandbox de WhatsApp y vincula tu número enviando el código de invitación al número de Twilio.
3. Edita `src/main.py` y reemplaza las credenciales:
   ```python
   ACCOUNT_SID = "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
   AUTH_TOKEN = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
   TO_NUMBER = "whatsapp:+58XXXXXXXXXX"
   ```

---

## ✅ Resultados esperados

- Reporte en consola con métricas de ventas.
- Gráficos en `output/`.
- Mensaje de WhatsApp con resumen y enlaces a gráficos.

---

## 👨‍💻 Autor

Proyecto desarrollado por **Alex Hernandez** como parte de la asignatura de Inteligencia Artificial (2025).
```

