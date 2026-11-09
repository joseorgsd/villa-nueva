import json
import os
from datetime import datetime

# Base de datos expandida para ofrecer más oportunidades
NUEVOS_LEADS = [
    {
        "id": 1,
        "nombre": "Logística del Sur S.A.",
        "industria": "Logística y Cadena de Suministro",
        "necesidad_detectada": "Actualización de software de gestión de inventario a la nube",
        "contacto": "Juan Pérez, Director de Operaciones",
        "email": "jperez@logisticadelsur.com",
        "valor_estimado_contrato": 15000,
        "probabilidad": "Alta"
    },
    {
        "id": 2,
        "nombre": "EducaTech Innovación",
        "industria": "Tecnología Educativa",
        "necesidad_detectada": "Implementación de IA para personalización de aprendizaje",
        "contacto": "María González, CEO",
        "email": "maria@educatech.io",
        "valor_estimado_contrato": 45000,
        "probabilidad": "Media"
    },
    {
        "id": 3,
        "nombre": "Hotelaria Premium Group",
        "industria": "Hospitalidad",
        "necesidad_detectada": "Sistema de reservas centralizado y análisis de datos de huéspedes",
        "contacto": "Carlos Ruiz, Gerente General",
        "email": "cruiz@hotelpremium.com",
        "valor_estimado_contrato": 22000,
        "probabilidad": "Alta"
    },
    {
        "id": 4,
        "nombre": "Fintech Global Solutions",
        "industria": "Servicios Financieros",
        "necesidad_detectada": "Automatización de cumplimiento normativo (KYC/AML) mediante APIs",
        "contacto": "Sofía Castro, CTO",
        "email": "scastro@fintechglobal.net",
        "valor_estimado_contrato": 60000,
        "probabilidad": "Alta"
    },
    {
        "id": 5,
        "nombre": "Salud Integral del Norte",
        "industria": "Salud y Bienestar",
        "necesidad_detectada": "Portal de pacientes con historias clínicas cifradas y recordatorios por IA",
        "contacto": "Dr. Javier Morales, Director Médico",
        "email": "jmorales@saludintegralnorte.cl",
        "valor_estimado_contrato": 35000,
        "probabilidad": "Media"
    }
]

def generate_leads():
    output_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, 'leads_generados.json')
    
    payload = {
        "fecha_generacion": datetime.now().isoformat(),
        "total_leads": len(NUEVOS_LEADS),
        "valor_potencial_total": sum(e['valor_estimado_contrato'] for e in NUEVOS_LEADS),
        "leads": NUEVOS_LEADS
    }
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(payload, f, indent=4, ensure_ascii=False)
    
    print(f"[OK] {len(NUEVOS_LEADS)} leads avanzados generados correctamente.")

if __name__ == '__main__':
    generate_leads()