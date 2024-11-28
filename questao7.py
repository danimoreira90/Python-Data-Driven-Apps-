from langchain_community.llms import FakeListLLM, HuggingFaceHub
from langchain_openai.chat_models import ChatOpenAI
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
import os
from langchain.schema import HumanMessage
from dotenv import load_dotenv
import sys
import io
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# def translate_using_huggingface_api(text):

#     llm = HuggingFaceEndpoint(
#         repo_id='Helsinki-NLP/opus-mt-en-fr',
#         huggingfacehub_api_token = os.getenv("HUGGINGFACEHUB_API_TOKEN"),
#         model_kwargs= {"temperature": 0.5, "max_length": 64},


#     # using the model 
#     output = llm.invoke('If you are going through hell, keep going.')

#     print(output)


# load_dotenv()
# def use_hugging_face_hub(text):
#     """
#     Use the HuggingFaceHub to generate responses
#     """
#     llm = HuggingFaceHub(
#         model_kwargs = {"temperature": 0.5, "max_length": 64},
#         repo_id = "Helsinki-NLP/opus-mt-en-de", 
#         huggingfacehub_api_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")
#     )
#     completation = llm.invoke(text)
#     print(completation)
    

# if __name__ == "__main__":

#     print("\n # Using HuggingFaceHub")
#     use_hugging_face_hub("If you are going through hell, keep going.")

app = FastAPI()

load_dotenv()  # Carrega variáveis de ambiente do arquivo .env

class TranslationRequest(BaseModel):
    text: str

@app.post("/translate/")
async def translate_text(request: TranslationRequest):
    if not request.text:
        raise HTTPException(status_code=400, detail="Text parameter is required.")
    
    # Instanciando o modelo de tradução
    llm = HuggingFaceHub(
        model_kwargs={"temperature": 0.5, "max_length": 64},
        repo_id="Helsinki-NLP/opus-mt-en-de",
        huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN")
    )
    
    # Realizando a tradução
    try:
        completion = llm.invoke(request.text)
        return {"translated_text": completion}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
