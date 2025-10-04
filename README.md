# Bingle Bongle

Bingle Bongle is a maximalist notes application designed for iOS that allows users to create and manage handwritten notes using PencilKit. The application features a user-friendly interface and integrates with a Python backend for advanced functionalities such as Gemini prompt handling and LaTeX OCR parsing.

## Features

- Handwritten note-taking with PencilKit
- Intuitive user interface for easy navigation
- Gemini prompt handling for enhanced note-taking
- LaTeX OCR parsing for converting handwritten notes into text

## Project Structure

```
bingle-bongle
├── ios
│   ├── BingleBongle
│   │   ├── AppDelegate.swift
│   │   ├── SceneDelegate.swift
│   │   ├── Assets.xcassets
│   │   ├── Info.plist
│   │   ├── Views
│   │   │   ├── MainView.swift
│   │   │   └── HandwritingView.swift
│   │   ├── Models
│   │   │   └── Note.swift
│   │   ├── Controllers
│   │   │   └── NoteController.swift
│   │   └── Utils
│   │       └── PencilKitHelper.swift
│   └── README.md
├── backend
│   ├── app
│   │   ├── main.py
│   │   ├── routes
│   │   │   ├── gemini.py
│   │   │   └── latex_ocr.py
│   │   ├── services
│   │   │   ├── gemini_service.py
│   │   │   └── latex_ocr_service.py
│   │   └── utils
│   │       └── helpers.py
│   ├── requirements.txt
│   └── README.md
└── README.md
```

## Getting Started

### iOS Application

1. Open the `ios/BingleBongle` project in Xcode.
2. Build and run the application on a compatible iOS device or simulator.
3. Use the main view to create and manage your handwritten notes.

### Python Backend

1. Navigate to the `backend` directory.
2. Install the required dependencies using:
   ```
   pip install -r requirements.txt
   ```
3. Run the backend server with:
   ```
   python app/main.py
   ```
4. Access the API endpoints for Gemini prompts and LaTeX OCR parsing.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.