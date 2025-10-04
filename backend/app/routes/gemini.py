from flask import Blueprint, request, jsonify
from app.services.gemini_service import GeminiService

gemini_bp = Blueprint('gemini', __name__)
gemini_service = GeminiService()

@gemini_bp.route('/gemini/prompt', methods=['POST'])
def handle_gemini_prompt():
    data = request.json
    prompt = data.get('prompt')

    if not prompt:
        return jsonify({'error': 'Prompt is required'}), 400

    response = gemini_service.process_prompt(prompt)
    return jsonify({'response': response}), 200