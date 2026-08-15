from langgraph.graph import StateGraph, START, END
from langchain_ollama import ChatOllama
from typing_extensions import TypedDict
from typing import Annotated
import operator

class State(TypedDict):
    topic: str
    plan: str
    worker1_res: str
    worker2_res: str
    final_output: Annotated[str, operator.add]

llm = ChatOllama(model="qwen2.5:7b")

def orchestrator(state):
    prompt = f"针对主题'{state['topic']}'，制定两个维度的研究规划。"
    return {"plan": llm.invoke(prompt).content}

def worker1(state):
    return {"worker1_res": llm.invoke(f"基于规划'{state['plan']}'进行维度一研究").content}

def worker2(state):
    return {"worker2_res": llm.invoke(f"基于规划'{state['plan']}'进行维度二研究").content}

def synthesizer(state):
    res = f"研究报告汇聚：\n1. {state['worker1_res']}\n2. {state['worker2_res']}"
    return {"final_output": res}

def buildGraph():
    builder = StateGraph(State)
    builder.add_node("orchestrator", orchestrator)
    builder.add_node("worker1", worker1)
    builder.add_node("worker2", worker2)
    builder.add_node("synthesizer", synthesizer)
    
    builder.add_edge(START, "orchestrator")
    builder.add_edge("orchestrator", "worker1")
    builder.add_edge("orchestrator", "worker2")
    builder.add_edge(["worker1", "worker2"], "synthesizer")
    builder.add_edge("synthesizer", END)
    return builder.compile()
