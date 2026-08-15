from langgraph.graph import StateGraph, START, END
from langchain_ollama import ChatOllama
from typing_extensions import TypedDict
from typing import Annotated
import operator

class State(TypedDict):
    topic: str
    view_a: str
    view_b: str
    summary: Annotated[str, operator.add]

llm = ChatOllama(model="qwen2.5:7b")

def node_a(state):
    return {"view_a": llm.invoke(f"针对{state['topic']}提出正面观点").content}

def node_b(state):
    return {"view_b": llm.invoke(f"针对{state['topic']}提出反面观点").content}

def buildGraph():
    builder = StateGraph(State)
    builder.add_node("node_a", node_a)
    builder.add_node("node_b", node_b)
    builder.add_edge(START, "node_a")
    builder.add_edge(START, "node_b")
    builder.add_edge(["node_a", "node_b"], END)
    return builder.compile()
