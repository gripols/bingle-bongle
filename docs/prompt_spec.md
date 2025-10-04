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
{ "note": "The limt of sin(x)/x as x -> 0 is 0" 

{
  "mistakes": [
    { "span": "limt", "fix": "limit", "type": "Spelling", "severity": 1 },
    { "span": "is 0", "fix": "is 1", "type": "Factual", "severity": 3 }
  ]
}

{ "text": "极限点", "target_lang": "en" }

{
  "translation": "limit point",
  "plain_en": "A limit point is a special point where other points from the set get very close.",
  "examples": ["For the set {1/2, 1/3, 1/4, ...}, 0 is a limit point."]
}

{ "expr": "integral from 0 to infinity of e^(-x^2) dx" }

{
  "latex": "\\int_0^\\infty e^{-x^2} dx",
  "description": "The definite integral of e to the power of negative x squared from 0 to infinity."
}

{ "note": "Limit, continuity, differentiability" }

{
  "cards": [
    {"term": "Limit", "definition": "The value a function approaches as input approaches a point."},
    {"term": "Continuity", "definition": "A function is continuous if small input changes make small output changes."}
  ]
}


