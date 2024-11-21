from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import pipeline
import os

app = FastAPI()

class TranslationRequest(BaseModel):
    text: str

# Carrega o modelo de tradução do HuggingFace Hub
translator = pipeline("translation_en_to_fr", model="Helsinki-NLP/opus-mt-en-fr")

@app.post("/translate/")
async def translate_text(request: TranslationRequest):
    if not request.text:
        raise HTTPException(status_code=400, detail="Text parameter is required.")
    
    try:
        # Traduz o texto para o francês
        translated_text = translator(request.text, max_length=512)
        # Retorna o texto traduzido em uma resposta JSON
        return {"translated_text": translated_text[0]['translation_text']}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
