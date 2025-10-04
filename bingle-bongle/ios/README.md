# Bingle Bongle iOS Application

Welcome to the Bingle Bongle iOS application! This project is designed to provide a maximalist note-taking experience with support for handwritten input using PencilKit. Below are the details for setting up and using the application.

## Features

- Handwritten note-taking with PencilKit
- Intuitive user interface for managing notes
- Robust backend integration for advanced functionalities

## Project Structure

The iOS application is structured as follows:

```
BingleBongle/
├── AppDelegate.swift       // Application lifecycle management
├── SceneDelegate.swift     // Scene-based UI lifecycle management
├── Assets.xcassets         // Image assets and resources
├── Info.plist              // Configuration settings
├── Views/
│   ├── MainView.swift      // Main user interface
│   └── HandwritingView.swift // Handwriting input view
├── Models/
│   └── Note.swift          // Note data model
├── Controllers/
│   └── NoteController.swift // Logic for note management
└── Utils/
    └── PencilKitHelper.swift // Utility functions for PencilKit
```

## Setup Instructions

1. **Clone the Repository**
   ```
   git clone https://github.com/yourusername/bingle-bongle.git
   cd bingle-bongle/ios
   ```

2. **Open the Project**
   Open the `BingleBongle.xcodeproj` file in Xcode.

3. **Build and Run**
   Select a simulator or a physical device and click on the run button in Xcode.

## Usage Guidelines

- **Creating Notes**: Navigate to the main view and use the provided interface to create new notes.
- **Handwriting Input**: Tap on the handwriting view to start writing with your Apple Pencil or finger.
- **Saving Notes**: Notes are automatically saved as you write, ensuring you never lose your work.

## Contributing

We welcome contributions! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

Thank you for using Bingle Bongle! Enjoy your note-taking experience!