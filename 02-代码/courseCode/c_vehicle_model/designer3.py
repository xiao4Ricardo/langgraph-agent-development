from langchain_core.runnables import Runnable
from typing import Dict, Optional
from langgraph.graph import StateGraph, START
from typing_extensions import TypedDict
from typing import Annotated
import operator
import os
from a_gather_infomation import getInfomation

class CustomModel(Runnable):
    def __init__(self, model_endpoint: str, api_key: str):
        self.endpoint = model_endpoint
        self.api_key = api_key

    def invoke(self, prompt: str, modelName:str="deepseek-ai/DeepSeek-V3",maxTokens:int=3000,tempreture=0.6,config: Optional[Dict] = None) -> Dict:
        import requests
        headers = {"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"}
        payload = {"model":modelName, "messages": [{"role": "user", "content": prompt}], "temperature":tempreture, "max_tokens": maxTokens}
        response = requests.post(self.endpoint, json=payload, headers=headers)
        response.raise_for_status()
        return response.json()['choices'][0]['message']['content']

llm = CustomModel(
    model_endpoint="https://api.siliconflow.cn/v1/chat/completions",
    api_key=os.getenv("SILICONFLOW_API_KEY", "your-siliconflow-api-key")
)

def generateChapter1(state):
    return state
