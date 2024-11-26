# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# from langchain_openai.chat_models import ChatOpenAI
# import os
# from langchain.schema import HumanMessage
# from dotenv import load_dotenv
# import sys
# import io

# sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
# sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')


# load_dotenv()
# def use_openai_api():
#     """
#     Use the OpenAI API to generate responses
#     """
#     llm = ChatOpenAI(model="gpt-4o", api_key=os.getenv("OPENAI_API_KEY"))
#     message = HumanMessage(content="Think about 5 different sentences related to energy efficiency and translate them to Japanese. Bring the used kanji in hiragana. Also translate them to french.")
#     response = llm.invoke([message])
#     print(response.content)




# if __name__ == "__main__":

#     print("# OpenAI")
#     use_openai_api()

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from langchain_openai.chat_models import ChatOpenAI
import os
from langchain.schema import HumanMessage
from dotenv import load_dotenv
import sys
import io

# Configurando codificação padrão
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

# Carrega as variáveis de ambiente
load_dotenv()

# Define o modelo de dados de entrada usando Pydantic
class TranslationRequest(BaseModel):
    content: str
    language: str

# Instancia o FastAPI
app = FastAPI()

# Define uma rota POST para a tradução
@app.post("/translate/")
async def translate(request: TranslationRequest):
    """
    Recebe uma mensagem e a traduz para o idioma especificado.
    """
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise HTTPException(status_code=500, detail="API Key is not set")

    # Instancia o LLM
    llm = ChatOpenAI(model="gpt-4o", api_key=api_key)

    # Cria a mensagem humana a ser enviada para o modelo
    message = HumanMessage(content=request.content)
    
    # Invoca o modelo e retorna a resposta
    response = llm.invoke([message])
    if response.success:
        return {"response": response.content}
    else:
        raise HTTPException(status_code=500, detail="Failed to generate response from the model")

# Remove a execução direta, pois agora a aplicação deve ser executada por um servidor ASGI
