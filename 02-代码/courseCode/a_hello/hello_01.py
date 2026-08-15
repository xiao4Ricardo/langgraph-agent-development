from langgraph.prebuilt import create_react_agent
from langchain_ollama import ChatOllama

agent = create_react_agent(
    model=ChatOllama(model="qwen2.5:7b"),
    tools=[],
    prompt=""
)

# Run the agent
result = agent.invoke(
    {"messages": [{"role": "user", "content": "你是谁？"}]}
)
print(result["messages"][-1].content)