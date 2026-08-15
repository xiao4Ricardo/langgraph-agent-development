from langgraph.graph import START,StateGraph,  END
from typing_extensions import TypedDict
from typing import Annotated
from langgraph.types import interrupt,Command
from langgraph.checkpoint.memory import InMemorySaver

def updateTempreture(left, right):
    return max(left, right)

def updateProduct(left,right):
    if left=="加糖咖啡" or right == "加糖咖啡":
        return "加糖咖啡"
    elif left=="咖啡" or right == "咖啡":
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
def updateSugur(left,right):
    if left=="是" or right == "是":
        return "是"
    else:
        return "否"

class State(TypedDict):
    水温: Annotated[int,updateTempreture]
    产物:Annotated[str,updateProduct]
    咖啡固体:Annotated[str,updateSolid]
    是否加糖:Annotated[str,updateSugur]

def 磨咖啡豆(state):
    state["咖啡固体"] = "咖啡粉"
    return state

def 烧水(state):
    state["水温"] = state["水温"]+10
    if state["水温"]>100:
        state["水温"] = 100
        state["产物"] = "开水"
    return state

def 按温度处理水(state):
    if state["水温"]== 100:
        return "水烧开了"
    else:
        return "水没开"

def 得到开水(state):
    return state

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

def buildGraph6():
    heatWaterSubGraphBuilder = StateGraph(State)
    heatWaterSubGraphBuilder.add_node("heat water", 烧水)
    heatWaterSubGraphBuilder.add_node("get boil water", 得到开水)
    heatWaterSubGraphBuilder.add_edge(START, "heat water")
    heatWaterSubGraphBuilder.add_conditional_edges("heat water", 按温度处理水,{"水烧开了": "get boil water", "水没开": "heat water"})
    heatWaterSubGraph = heatWaterSubGraphBuilder.compile()

    addSugurSubGraphBuilder = StateGraph(State)
    checkpointer = InMemorySaver()
    addSugurSubGraphBuilder.add_node("询问是否加糖1", 询问是否加糖)
    addSugurSubGraphBuilder.add_node("加糖", 加糖)
    addSugurSubGraphBuilder.add_edge(START,"询问是否加糖1")
    addSugurSubGraphBuilder.add_conditional_edges("询问是否加糖1", 是否加糖分支, {"是": "加糖", "否": END})
    addSugurSubGraph = addSugurSubGraphBuilder.compile(checkpointer=checkpointer)

    graphBuilder = StateGraph(State)
    graphBuilder.add_node("得到热水子图",heatWaterSubGraph)
    graphBuilder.add_node("磨咖啡豆", 磨咖啡豆)
    graphBuilder.add_node("冲咖啡", 冲咖啡)
    graphBuilder.add_node("加糖子图1", addSugurSubGraph)
    graphBuilder.add_edge(START,"得到热水子图")
    graphBuilder.add_edge(START, "磨咖啡豆")
    graphBuilder.add_edge(["得到热水子图","磨咖啡豆"],"冲咖啡")
    graphBuilder.add_edge("冲咖啡","加糖子图1")
    graph = graphBuilder.compile(checkpointer=checkpointer)
    return heatWaterSubGraph,addSugurSubGraph,graph
