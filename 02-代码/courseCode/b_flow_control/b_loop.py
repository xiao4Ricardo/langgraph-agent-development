from langgraph.graph import START,StateGraph,  END
from typing_extensions import TypedDict

class State(TypedDict):
    count: int

def loopNode(state):
    state["count"] = state.get("count", 0) + 1
    return state

def shouldContinue(state):
    if state["count"] >= 5:
        return END
    return "loopNode"

def buildGraph():
    builder = StateGraph(State)
    builder.add_node("loopNode", loopNode)
    builder.add_edge(START, "loopNode")
    builder.add_conditional_edges("loopNode", shouldContinue)
    return builder.compile()
