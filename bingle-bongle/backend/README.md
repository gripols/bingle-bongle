# Bingle Bongle Backend Documentation

## Overview
Bingle Bongle is a notes application that allows users to create and manage handwritten notes using PencilKit on iOS. The backend is built with Python and provides essential functionalities such as Gemini prompt handling and LaTeX OCR parsing.

## Project Structure
The backend is organized into the following directories and files:

- **app/**: Contains the main application code.
  - **main.py**: Entry point for the backend application.
  - **routes/**: Contains route definitions for handling API requests.
    - **gemini.py**: Routes for Gemini prompt requests.
    - **latex_ocr.py**: Routes for LaTeX OCR parsing requests.
  - **services/**: Contains service classes that encapsulate business logic.
    - **gemini_service.py**: Logic for processing Gemini prompts.
    - **latex_ocr_service.py**: Manages OCR parsing functionality.
  - **utils/**: Contains utility functions used across the application.
    - **helpers.py**: General helper functions.

- **requirements.txt**: Lists the Python dependencies required for the backend application.

## Setup Instructions
1. Clone the repository:
   ```
   git clone <repository-url>
   cd bingle-bongle/backend
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Run the application:
   ```
   python app/main.py
   ```

## API Usage
The backend exposes several endpoints for interacting with the application:

### Gemini Prompt Handling
- **POST /gemini**: Accepts a Gemini prompt and returns a response based on the input.

### LaTeX OCR Parsing
- **POST /latex_ocr**: Accepts an image containing LaTeX and returns the parsed LaTeX code.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.