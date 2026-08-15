from langgraph.graph import START,StateGraph,  END
from typing_extensions import TypedDict
from langgraph.types import Command, interrupt
from langgraph.checkpoint.memory import InMemorySaver

class State(TypedDict):
    产物:str
    是否加糖:str

def 冲咖啡(state):
    state["产物"]="咖啡"
    return state

def 询问是否加糖(state):
    human_response = interrupt("")
    state["是否加糖"] = human_response
    return state

def 是否加糖分支(state):
    if state["是否加糖"] == "是":
        return "是"
    elif state["是否加糖"] == "否":
        return "否"

def 加糖(state):
    state["产物"]="加糖咖啡"
    return state

def buildGraph():
    graphBuilder = StateGraph(State)
    checkpointer = InMemorySaver()
    graphBuilder.add_node("冲咖啡", 冲咖啡)
    graphBuilder.add_node("询问是否加糖", 询问是否加糖)
    graphBuilder.add_node("加糖", 加糖)
    graphBuilder.add_edge(START, "冲咖啡")
    graphBuilder.add_edge("冲咖啡", "询问是否加糖")
    graphBuilder.add_conditional_edges("询问是否加糖", 是否加糖分支,{"是":"加糖","否":END})
    graphBuilder.add_edge("加糖", END)
    return graphBuilder.compile(checkpointer=checkpointer)
