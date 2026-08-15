from langgraph.graph import StateGraph, START, END
from langchain_ollama import ChatOllama
from typing_extensions import TypedDict
import json

class State(TypedDict):
    topic:str
    article:str
    feedback:str
    qualified:str
    count:int

llm = ChatOllama(model="qwen2.5:7b")

def generate(state):
    if state.get("feedback"):
        prompt = """根据提供的主题写一篇论证文章。主题为"""+state["topic"]+"""\n修改建议："""+state["feedback"]
    else:
        prompt = """根据提供的主题写一篇论证文章。主题为""" + state["topic"]
    result = llm.invoke(prompt)
    state["count"] += 1
    state["article"] = result.content
    return state

def evaluate(state):
    prompt = """判断文章是否严密。按照格式输出: {"是否合格":"是/否", "修改意见":""}\n主题:"""+state["topic"]+"""\n文章:"""+state["article"]
    result = llm.invoke(prompt)
    try:
        resultJson = json.loads(result.content)
        state["qualified"] = resultJson.get("是否合格", "否")
        state["feedback"] = resultJson.get("修改意见", "")
    except Exception:
        state["qualified"] = "是"
    return state

def judgement(state):
    if state["count"] >= 5 or state["qualified"] == "是":
        return "accept"
    return "reject"

def buildGraph():
    graphBuilder = StateGraph(State)
    graphBuilder.add_node("generate", generate)
    graphBuilder.add_node("evaluate", evaluate)
    graphBuilder.add_edge(START, "generate")
    graphBuilder.add_edge("generate", "evaluate")
    graphBuilder.add_conditional_edges("evaluate",judgement, {"accept":END,"reject":"generate"})
    return graphBuilder.compile()
