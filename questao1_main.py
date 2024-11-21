from fastapi import FastAPI, HTTPException
from transformers import pipeline
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    text: str

generator = pipeline('text-generation', model='gpt2')

@app.post("/generate/")
async def generate_text(item: Item):
    if not item.text:
        raise HTTPException(status_code=400, detail="Text parameter is required.")
    generated_text = generator(item.text, max_length=100, num_return_sequences=1)
    return {"generated_text": generated_text[0]['generated_text']}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)