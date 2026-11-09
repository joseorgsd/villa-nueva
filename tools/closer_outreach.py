"""
Script de Cierre de Ventas (Outreach Closer)
Genera el mensaje exacto para enviar por WhatsApp o Email al dueño del negocio.
"""

import sys

def generate_message(nombre_negocio, nombre_dueno, url_web):
    mensaje = f"""
Hola {nombre_dueno}, ¿cómo estás?

Estuve revisando la web de {nombre_negocio} ({url_web}) y noté que está perdiendo clientes potenciales debido a problemas de velocidad y posicionamiento en Google (su web carga lenta en celulares).

Hice una auditoría rápida de 10 puntos clave de su negocio de forma gratuita:
[ Adjuntar o pegar el informe generado en reports/ ]

Ayudo a negocios locales como el suyo a modernizar su presencia digital para que reciban más llamadas y clientes cada semana. 

¿Tendrías 5 minutos esta semana para mostrarte cómo podríamos solucionarlo?

Un saludo,
[Tu Nombre]
Especialista en Crecimiento Digital
"""
    return mensaje.strip()

if __name__ == "__main__":
    print("--- Generador de Mensaje de Cierre ---")
    negocio = input("Nombre del negocio (ej. Restaurante El Buen Sabor): ")
    dueno = input("Nombre del dueño/contacto (ej. Carlos): ")
    web = input("Sitio web actual (ej. www.elbuensabor.com): ")
    
    print("\n" + "="*40 + "\n")
    print(generate_message(negocio, dueno, web))
    print("\n" + "="*40)
