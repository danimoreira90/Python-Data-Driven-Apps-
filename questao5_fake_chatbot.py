from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from langchain_community.llms import FakeListLLM

app = FastAPI()

# Definindo um modelo base de dados para a entrada
class ChatInput(BaseModel):
    message: str

# Criando uma instância do FakeListLLM com respostas pré-definidas
fake_llm = FakeListLLM(responses=[
    "Sup bra. How's it goin'?",
    "U mirin'?",
    "What's crackin'?"
])

@app.post("/chat/")
async def chat(input: ChatInput):
    if not input.message:
        raise HTTPException(status_code=400, detail="Message parameter is required.")
    # Invocar o FakeListLLM para obter uma resposta
    response = fake_llm.invoke(input.message)
    return {"response": response}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=5000)
