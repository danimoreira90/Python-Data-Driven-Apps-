from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from langchain_openai.chat_models import ChatOpenAI
import os
from langchain.schema import HumanMessage
from dotenv import load_dotenv
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')


load_dotenv()
def use_openai_api():
    """
    Use the OpenAI API to generate responses
    """
    llm = ChatOpenAI(model="gpt-4o", api_key=os.getenv("OPENAI_API_KEY"))
    message = HumanMessage(content="Think about 5 different sentences related to energy efficiency and translate them to Japanese. Bring the used kanji in hiragana. Also translate them to french.")
    response = llm.invoke([message])
    print(response.content)




if __name__ == "__main__":

    print("# OpenAI")
    use_openai_api()
