from langgraph.graph import START,StateGraph,END

graphBuilder = StateGraph(dict)
graphBuilder.add_edge(START, END)
graph = graphBuilder.compile()
