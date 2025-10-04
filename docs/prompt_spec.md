# Prompt Kit Specification

**Author:** Rose-sys-collan  
**Module:** bingle-bongle/ai/promptKit.py  
**Model:** `models/gemini-2.5-flash`

---

## 1. Overview

This prompt kit supports 4 AI-enhanced features for the note-taking app:

| Feature | Description |
|----------|--------------|
| ① Mistake Detection | Detect common conceptual/spelling errors and return structured feedback |
| ② Translate + Explain | Translate Chinese ↔ English with simplified plain-English explanation |
| ③ Math → LaTeX | Convert handwritten or plain-text math into LaTeX syntax with descriptions |
| ④ Study Cards | Generate Anki/Quizlet-compatible flashcards for key terms |

---

## 2. API Contracts

### `/api/mistakes`
**Request**
```json
{ "note": "The limt of sin(x)/x as x -> 0 is 0" }
```
**Response**
```json
{
  "mistakes": [
    { "span": "limt", "fix": "limit", "type": "Spelling", "severity": 1 },
    { "span": "is 0", "fix": "is 1", "type": "Factual", "severity": 3 }
  ]
}
```

### `/api/translate`
**Request**
```json
{ "text": "极限点", "target_lang": "en" }
```
**Response**
```json
{
  "translation": "limit point",
  "plain_en": "A limit point is a special point where other points from the set get very close.",
  "examples": ["For the set {1/2, 1/3, 1/4, ...}, 0 is a limit point."]
}
```

### `/api/latex`
**Request**
```json
{ "expr": "integral from 0 to infinity of e^(-x^2) dx" }
```
**Response**
```json
{
  "latex": "\\int_0^\\infty e^{-x^2} dx",
  "description": "The definite integral of e to the power of negative x squared from 0 to infinity."
}
```

### `/api/cards`
**Request**
```json
{ "note": "Limit, continuity, differentiability" }
```
**Response**
```json
{
  "cards": [
    {"term": "Limit", "definition": "The value a function approaches as input approaches a point."},
    {"term": "Continuity", "definition": "A function is continuous if small input changes make small output changes."}
  ]
}
```

---

## 3. Backend Python API Endpoints

- `/api/mistakes` (POST): Analyze note for mistakes.
- `/api/translate` (POST): Translate and explain terms.
- `/api/latex` (POST): Convert math to LaTeX.
- `/api/cards` (POST): Generate study cards.

All endpoints accept and return JSON.

---

## 4. Anki Card Graphic Elements

To enhance the study experience, each generated card can include:

- **Icon**: A relevant emoji or SVG (e.g., 📐 for math, 🌐 for language).
- **Color Accent**: Use a color band or background based on card type (e.g., blue for math, green for language).
- **LaTeX Rendering**: If the card contains LaTeX, render it using MathJax or KaTeX in the frontend.
- **Example Illustration**: If available, show a small SVG or PNG illustration (auto-generated or user-uploaded).
- **Responsive Layout**: Cards should look good on mobile and desktop, with clear separation between term and definition.

**Example Card Layout:**

```
+---------------------------------------------+
| 📐  Limit                                  |
|---------------------------------------------|
| The value a function approaches as input    |
| approaches a point.                        |
|                                             |
| [LaTeX: \lim_{x\to a} f(x)]                |
+---------------------------------------------+
```

---

## 5. Security & Data Handling

- No user data is stored on the backend unless explicitly required for processing.
- All endpoints validate input and sanitize outputs.
- No sensitive information is logged or persisted.

---


