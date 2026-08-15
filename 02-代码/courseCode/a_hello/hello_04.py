from langgraph.prebuilt import create_react_agent
from langchain_ollama import ChatOllama
from langchain_core.messages import AnyMessage

def getPrompt(state,config) -> list[AnyMessage]:
    company = config["configurable"].get("company")
    systemMsg = "你是"+company+"训练的智能销售助理"
    return [{"role": "system", "content": systemMsg}] + state["messages"]


agent = create_react_agent(
    model=ChatOllama(model="qwen2.5:7b",temperature = 0.8),
    tools=[],
    prompt=getPrompt
)

# Run the agent
result = agent.invoke(
    {"messages": [{"role": "user", "content": "你是谁？"}]},
          config={"configurable": {"company": "诚通智能"}}
)
print(result["messages"][-1].content)

result = agent.invoke(
    {"messages": [{"role": "user", "content": "你是谁？"}]},
          config={"configurable": {"company": "凯瑞汽车"}}
)
print(result["messages"][-1].content)