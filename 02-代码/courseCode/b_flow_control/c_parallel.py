from langgraph.graph import START,StateGraph,  END
from typing_extensions import TypedDict
from typing import Annotated

def updateTempreture(left, right):
    return max(left, right)

def updateProduct(left,right):
    if left=="咖啡" or right == "咖啡":
        return "咖啡"
    elif left=="开水" or right == "开水":
        return "开水"
    elif left=="温水" or right == "温水":
        return "温水"
    else:
        return "凉水"

def updateSolid(left,right):
    if left=="咖啡粉" or right == "咖啡粉":
        return "咖啡粉"
    else:
        return "咖啡豆"

class State(TypedDict):
    水温: Annotated[int,updateTempreture]
    产物:Annotated[str,updateProduct]
    咖啡固体:Annotated[str,updateSolid]

def 磨咖啡豆(state):
    state["咖啡固体"] = "咖啡粉"
    return state

def 烧温水(state):
    if state["水温"]<38:
        state["水温"] = 38
        state["产物"] = "温水"
    return state

def 烧开水(state):
    if state["水温"]<100:
        state["水温"] = 100
        state["产物"] = "开水"
    return state

def 冲咖啡(state):
    state["产物"]="咖啡"
    return state

def buildGraph3():
    graphBuilder = StateGraph(State)
    graphBuilder.add_node("烧水1", 烧温水)
    graphBuilder.add_node("烧水2", 烧开水)
    graphBuilder.add_node("磨咖啡豆", 磨咖啡豆)
    graphBuilder.add_node("冲咖啡", 冲咖啡)
    graphBuilder.add_edge(START, "磨咖啡豆")
    graphBuilder.add_edge(START, "烧水1")
    graphBuilder.add_edge("烧水1", "烧水2")
    graphBuilder.add_edge(["烧水2","磨咖啡豆"], "冲咖啡")
    graphBuilder.add_edge("冲咖啡", END)
    return graphBuilder.compile()
