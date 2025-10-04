def extract_text_from_image(image_path):
    # Placeholder function for extracting text from an image using OCR
    # This function should implement the actual OCR logic
    pass

def validate_gemini_prompt(prompt):
    # Validate the Gemini prompt to ensure it meets the required format
    if isinstance(prompt, str) and len(prompt) > 0:
        return True
    return False

def format_response(data):
    # Format the response data into a standard structure
    return {
        "status": "success",
        "data": data
    }

def card_icon_for_term(term):
    # Return an emoji or SVG string based on the term type
    if any(x in term.lower() for x in ["limit", "integral", "derivative", "sum"]):
        return "📐"
    if any(x in term.lower() for x in ["language", "translate", "word"]):
        return "🌐"
    return "📝"