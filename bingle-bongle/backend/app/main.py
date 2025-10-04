from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.gemini import router as gemini_router
from routes.latex_ocr import router as latex_ocr_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(gemini_router, prefix="/gemini", tags=["Gemini"])
app.include_router(latex_ocr_router, prefix="/latex", tags=["LaTeX OCR"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Bingle Bongle backend!"}