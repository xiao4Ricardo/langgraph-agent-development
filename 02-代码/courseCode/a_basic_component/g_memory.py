from langgraph.graph import StateGraph, START,END
from langchain_ollama import ChatOllama
from typing_extensions import TypedDict
from typing import Annotated
from langgraph.graph.message import add_messages
from langgraph.checkpoint.memory import MemorySaver

class State(TypedDict):
    messages: Annotated[list, add_messages]

llm = ChatOllama(model="qwen2.5:7b")

def chatbot(state: State):
    return {"messages": [llm.invoke(state["messages"])]}

def buildGraphWithMemory():
    graphBuilder = StateGraph(State)
    memory = MemorySaver()
    graphBuilder.add_node("chatbot", chatbot)
    graphBuilder.add_edge(START, "chatbot")
    graphBuilder.add_edge("chatbot",END)
    graph = graphBuilder.compile(checkpointer=memory)
    return graph
