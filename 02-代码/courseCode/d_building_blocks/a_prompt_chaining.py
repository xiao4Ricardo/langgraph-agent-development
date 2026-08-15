from langgraph.graph import StateGraph, START,END
from langchain_ollama import ChatOllama
from typing_extensions import TypedDict

class State(TypedDict):
    topic:str
    outline:str
    draft:str
    paper:str

llm = ChatOllama(model="qwen2.5:7b")

def getOutline(state):
    prompt = """针对“"""+state["topic"]+"""”这个主题，写一份分析报告的大纲，包括历史由来，现状分析，原因分析，解决办法，趋势评估等几个主要部分。"""
    state["outline"]=llm.invoke(prompt).content
    return state

def getDraft(state):
    prompt = """根据【大纲】，写一份完整的分析报告，要求语言流畅，逻辑清晰，主要内容围绕大纲展开，内容2000字左右。
    
    【大纲】
    """+state["outline"]
    state["draft"]=llm.invoke(prompt).content
    return state

def getPaper(state):
    prompt = """请对下面的【分析报告】进行全文润色，包括语法检查，用词优化和句式调整，要求文章语言风格自然流畅，逻辑清晰，表达生动而简洁，避免生硬而刻板的AI习作风格，与原文的主要意思保持不变。
    
        【分析报告】
        """ + state["draft"]
    state["paper"] = llm.invoke(prompt).content
    return state

def buildGraph():
    graphBuilder = StateGraph(State)
    graphBuilder.add_node("getOutline", getOutline)
    graphBuilder.add_node("getDraft", getDraft)
    graphBuilder.add_node("getPaper", getPaper)
    graphBuilder.add_edge(START, "getOutline")
    graphBuilder.add_edge("getOutline", "getDraft")
    graphBuilder.add_edge("getDraft", "getPaper")
    graphBuilder.add_edge("getPaper",END)
    return graphBuilder.compile()
