from twilio.rest import Client

def send_whatsapp_message(account_sid, auth_token, to_number, body, media_urls=None):
    """
    Envía un mensaje de WhatsApp usando Twilio.
    - account_sid: SID de la cuenta Twilio
    - auth_token: Token de autenticación
    - to_number: Número destino en formato 'whatsapp:+58XXXXXXXXXX'
    - body: Texto del mensaje
    - media_urls: Lista de URLs de imágenes (opcional)
    """
    try:
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            from_="whatsapp:+14155238886",  # número sandbox de Twilio
            body=body,
            to=to_number,
            media_url=media_urls if media_urls else None
        )

        print(f"✅ Mensaje enviado. SID: {message.sid}")
    except Exception as e:
        print(f"❌ Error al enviar mensaje: {e}")