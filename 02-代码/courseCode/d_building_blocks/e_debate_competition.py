from langgraph.graph import StateGraph, START, END
from langchain_ollama import ChatOllama
from typing_extensions import TypedDict

class State(TypedDict):
    topic: str
    pro_argument: str
    con_argument: str
    judgement: str

llm = ChatOllama(model="qwen2.5:7b")

def pro_node(state):
    return {"pro_argument": llm.invoke(f"作为正方，对'{state['topic']}'阐述辩词。").content}

def con_node(state):
    return {"con_argument": llm.invoke(f"作为反方，对'{state['topic']}'阐述辩词。").content}

def judge_node(state):
    prompt = f"总结辩论：\n正方: {state['pro_argument']}\n反方: {state['con_argument']}"
    return {"judgement": llm.invoke(prompt).content}

def buildGraph():
    builder = StateGraph(State)
    builder.add_node("pro_node", pro_node)
    builder.add_node("con_node", con_node)
    builder.add_node("judge_node", judge_node)
    builder.add_edge(START, "pro_node")
    builder.add_edge(START, "con_node")
    builder.add_edge(["pro_node", "con_node"], "judge_node")
    builder.add_edge("judge_node", END)
    return builder.compile()
