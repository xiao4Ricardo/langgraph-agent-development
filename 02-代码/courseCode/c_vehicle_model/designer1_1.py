from a_gather_infomation import getInfomation
from langchain_ollama import ChatOllama

llm = ChatOllama(model="qwen2.5:7b")

state = {}
state = getInfomation(state)
prompt = "你是车型设计师，请完成新车型设计方案。"
