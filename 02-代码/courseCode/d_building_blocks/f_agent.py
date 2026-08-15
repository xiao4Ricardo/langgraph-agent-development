from langchain_ollama import ChatOllama
from langgraph.prebuilt import create_react_agent

def getTrainSchedule(queryDate,start,end):
    """查询列车班次"""
    return f"查询到 {queryDate} 从 {start} 到 {end} 的 D81 次列车。"

def getAvailableHotel(queryDate,location):
    """查询可用的旅店"""
    return f"查询到 {queryDate} 在 {location} 的丽晶酒店可以预定。"

toolList = [getTrainSchedule, getAvailableHotel]

agent = create_react_agent(
    model=ChatOllama(model="qwen3:8b"),
    tools=toolList,
    prompt=""
)
