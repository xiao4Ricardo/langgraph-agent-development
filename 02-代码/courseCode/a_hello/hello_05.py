from langgraph.prebuilt import create_react_agent
from langchain_ollama import ChatOllama

def getId() -> str:
    """explain your identity"""
    return f"我是凯瑞汽车训练的智能销售助理"

def getPriceByItem(item):
    """根据车名查询价格"""
    priceTable= {"月光女神":"135000",
                 "黑猫":"243000",
                 "飞扬":"175000"}
    if item in priceTable:
        return item+"的单价是："+priceTable[item]


agent = create_react_agent(
    model=ChatOllama(model="qwen2.5:7b",temperature = 0.8),
    tools=[getId,getPriceByItem]
)



prompt1 = "月光女神这款车多少钱？"
print("user:"+prompt1)
result = agent.invoke(
    {"messages": [{"role": "user", "content": prompt1}]}
)
print("assistant:"+result["messages"][-1].content)

prompt2 = "那飞扬呢？"
print("user:"+prompt2)
result = agent.invoke(
    {"messages": [{"role": "user", "content":prompt2 }]}
)
print("assistant:"+result["messages"][-1].content)