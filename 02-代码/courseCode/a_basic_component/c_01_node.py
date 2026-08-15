from langgraph.graph import StateGraph,START,  END
from typing_extensions import TypedDict

class State(TypedDict):
    x: int
    query:str
    answer:str

def add(state):
    state["y"] = state["x"]+1
    return state

from langgraph.prebuilt import create_react_agent
from langchain_ollama import ChatOllama

llm = ChatOllama(model="qwen2.5:7b", temperature=0.6)

def get_weather(city: str) -> str:
    return f"It's always sunny in {city}!"

def configLLM(state):
    agent = create_react_agent(
        model=llm,
        tools=[get_weather],
        prompt="You are a helpful assistant"
    )
    result = agent.invoke(
        {"messages": [{"role": "user", "content": state["query"]}]}
    )
    state["answer"] = result["messages"][-1].content
    return state
