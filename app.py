"""
Villa Nueva - Micro-SaaS Generator
Aplicación Flask para generar contenido y landing pages automatizadas.

Endpoints principales:
- GET /: Dashboard principal
- POST /generate: Genera contenido a partir de plantillas
- GET /health: Health check para deployment
"""

import os
import json
import subprocess
from datetime import datetime
from flask import Flask, render_template, request, jsonify, send_from_directory

app = Flask(__name__)
app.config['SECRET_KEY'] = 'villa-nueva-premium-2026'

DATA_FILE = os.path.join(os.path.dirname(__file__), 'data', 'leads_generados.json')

def get_leads_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {"total_leads": 0, "valor_potencial_total": 0, "leads": []}

@app.route('/')
def index():
    data = get_leads_data()
    return render_template('index.html', 
                           leads=data.get('leads', []),
                           stats={
                               'total': data.get('total_leads', 0),
                               'value': data.get('valor_potencial_total', 0)
                           },
                           title="Villa Nueva Intelligence",
                           version="1.1.0")

@app.route('/api/analyze')
def analyze_market():
    data = get_leads_data()
    leads = data.get('leads', [])
    
    # Análisis simple de mercado por industria
    industrias = {}
    for lead in leads:
        ind = lead['industria']
        industrias[ind] = industrias.get(ind, 0) + lead['valor_estimado_contrato']
        
    return jsonify({
        'segmentacion': industrias,
        'mensaje': 'Análisis de mercado realizado con éxito.'
    })

@app.route('/api/email/<int:lead_id>')
def get_email_draft(lead_id):
    data = get_leads_data()
    leads = data.get('leads', [])
    lead = next((l for l in leads if l['id'] == lead_id), None)
    
    if not lead:
        return jsonify({'error': 'Lead no encontrado'}), 404
        
    subject = f"Solución para {lead['necesidad_detectada']} - {lead['nombre']}"
    body = f"Estimado/a {lead['contacto'].split(',')[0].split()[-1]},\n\n" \
           f"He visto que {lead['nombre']} está buscando soluciones para {lead['necesidad_detectada']}. " \
           f"En Villa Nueva ayudamos a empresas de la industria {lead['industria']} a optimizar sus operaciones.\n\n" \
           f"¿Le vendría bien una llamada de 15 minutos esta semana?\n\n" \
           f"Saludos,\n" \
           f"Equipo Villa Nueva"
           
    return jsonify({
        'subject': subject,
        'body': body,
        'mailto': f"mailto:{lead['email']}?subject={subject}&body={body.replace('\n', '%0D%0A')}"
    })

# Endpoint de generación de contenido
@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    
    if not data or 'template' not in data:
        return jsonify({
            'error': 'Parámetro "template" requerido',
            'status': 'error'
        }), 400
    
    template = data['template']
    context = data.get('context', {})
    
    # Lógica simple de generación basada en plantillas
    generated = {
        'id': f"gen_{datetime.now().timestamp()}",
        'template': template,
        'context': context,
        'generado_en': datetime.now().isoformat(),
        'contenido': render_template(f'{template}.html', **context)
    }
    
    return jsonify({
        'status': 'success',
        'data': generated
    })

@app.route('/api/live-audit', methods=['POST'])
def live_audit():
    data = request.get_json()
    url = data.get('url')
    if not url:
        return jsonify({'error': 'URL requerida'}), 400
    
    try:
        # Ejecutar el auditor discreto
        # El auditor guarda en ../reports/, pero desde app.py (raíz) es ./reports/
        subprocess.run(['python', 'tools/web_auditor.py', '--url', url], check=True)
        
        # Construir el nombre del archivo igual que en web_auditor.py
        file_name = url.replace("https://", "").replace("http://", "").replace("/", "_") + "_audit.md"
        report_path = os.path.join(os.path.dirname(__file__), 'reports', file_name)
        
        if os.path.exists(report_path):
            with open(report_path, 'r', encoding='utf-8') as f:
                content = f.read()
            return jsonify({'status': 'success', 'report': content})
        else:
            return jsonify({'error': 'Error al generar el reporte'}), 500
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Health check
@app.route('/health')
def health():
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'service': 'Villa Nueva Generator'
    })

# Servir archivos estáticos
@app.route('/static/<path:path>')
def static_files(path):
    return send_from_directory('static', path)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)