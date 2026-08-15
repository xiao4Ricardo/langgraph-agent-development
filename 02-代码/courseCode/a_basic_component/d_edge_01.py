from langgraph.graph import START,StateGraph,  END
from typing_extensions import TypedDict

class State(TypedDict):
    tempreture: int

def heatUp(state):
    state["tempreture"] = state["tempreture"]+10
    if state["tempreture"]>100:
        state["tempreture"] = 100
    return state

def processWater(state):
    if state["tempreture"]== 100:
        return "hotWaterReady"
    else:
        return "stillCode"

def getBolidWater(state):
    return state

def buildGraph():
    graphBuilder = StateGraph(State)
    graphBuilder.add_node("heatUp", heatUp)
    graphBuilder.add_node("getBolidWater", getBolidWater)
    graphBuilder.add_edge(START, "heatUp")
    graphBuilder.add_conditional_edges("heatUp",processWater,{"hotWaterReady":"getBolidWater","stillCode":"heatUp"})
    graphBuilder.add_edge("getBolidWater",END)
    graph = graphBuilder.compile()
    return graph
