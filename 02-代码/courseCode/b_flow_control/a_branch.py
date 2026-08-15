from langgraph.graph import START,StateGraph,  END
from typing_extensions import TypedDict

class State(TypedDict):
    tempreture: int
    product: str

def heatUp(state):
    state["tempreture"] = state["tempreture"]+10
    return state

def branch_func(state):
    if state["tempreture"] >= 100:
        return "boil"
    else:
        return "cold"

def buildGraph():
    graphBuilder = StateGraph(State)
    graphBuilder.add_node("heatUp", heatUp)
    graphBuilder.add_edge(START, "heatUp")
    graphBuilder.add_conditional_edges("heatUp", branch_func, {"boil": END, "cold": "heatUp"})
    return graphBuilder.compile()
