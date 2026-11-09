"""
Preparador de Campaña de Ventas (Outreach)
Genera textos de correo personalizados a partir de los leads detectados.

Uso: python tools/outreach_preparator.py
Salida: data/campania_generada.md
"""

import json
import os

def generate_outreach_emails():
    """Lee los leads y genera plantillas de correo de venta."""
    data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
    leads_path = os.path.join(data_dir, 'leads_generados.json')
    
    if not os.path.exists(leads_path):
        print("[ERROR] Primero ejecuta lead_generator.py para generar los leads.")
        return

    with open(leads_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    output_dir = os.path.join(os.path.dirname(__file__), '..', 'docs')
    os.makedirs(output_dir, exist_ok=True)
    
    output_path = os.path.join(output_dir, 'campania_generada.md')
    
    template_header = """# Campaña de Outreach Generada
Fecha: {fecha}
Total de correos preparados: {total}

---

""".format(fecha=data['fecha_generacion'][:10], total=data['total_leads'])

    emails_md = []

    for lead in data['leads']:
        email_template = f"""
## Lead: {lead['nombre']}
**Contacto:** {lead['contacto']} | **Email:** {lead['email']}
**Industria:** {lead['industria']}
**Necesidad detectada:** {lead['necesidad_detectada']}
**Valor estimado:** ${lead['valor_estimado_contrato']:,} | **Probabilidad:** {lead['probabilidad']}

### Propuesta de Correo Electrónico:

**Asunto:** Solución para {lead['necesidad_detectada']} - {lead['nombre']}

**Cuerpo:**
Estimado/a {lead['contacto'].split(',')[0].split()[-1]},

He visto que {lead['nombre']} está buscando soluciones para {lead['necesidad_detectada']}. En [Tu Empresa] ayudamos a empresas de la industria {lead['industria']} a optimizar sus operaciones y escalar sus ingresos.

Me gustaría agendar una breve llamada de 15 minutos para analizar cómo podríamos abordar este desafío específico para ustedes.

¿Le vendría bien un tiempo esta semana?

Saludos cordiales,
[Tu Nombre]
[Tu Cargo]
[Tu Empresa]

---

"""
        emails_md.append(email_template)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(template_header + "\n".join(emails_md))
        
    print(f"[OK] Campaña generada exitosamente en: {output_path}")
    print(f"[INFO] Correos listos para revisar y personalizar.")

if __name__ == "__main__":
    generate_outreach_emails()