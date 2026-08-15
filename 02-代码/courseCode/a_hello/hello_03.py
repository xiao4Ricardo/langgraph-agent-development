from langgraph.prebuilt import create_react_agent
from langchain_ollama import ChatOllama

def getId() -> str:
    """explain your identity"""
    return f"我是凯瑞汽车训练的智能销售助理"

agent = create_react_agent(
    model=ChatOllama(model="qwen2.5:7b",temperature = 0.8),
    tools=[getId],
    prompt=""
)

for i in range(10):
    # Run the agent
    result = agent.invoke(
        {"messages": [{"role": "user", "content": "你是谁？"}]}
    )
    print(result["messages"][-1].content)