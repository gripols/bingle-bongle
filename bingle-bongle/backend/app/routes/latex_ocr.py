from flask import Blueprint, request, jsonify
from services.latex_ocr_service import LaTeXOCRService

latex_ocr_bp = Blueprint('latex_ocr', __name__)
ocr_service = LaTeXOCRService()

@latex_ocr_bp.route('/ocr', methods=['POST'])
def parse_latex():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    try:
        result = ocr_service.parse(file)
        return jsonify({'parsed_latex': result}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500