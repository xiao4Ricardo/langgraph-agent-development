from pydantic import BaseModel
from langgraph.prebuilt import create_react_agent
from langchain_ollama import ChatOllama


class PriceResponse(BaseModel):
    carType: str
    price:int

class PriceResponseList(BaseModel):
    priceResponseList: list[PriceResponse]

def getPriceByItem(item):
    """根据车名查询价格"""
    priceTable= {"月光女神":"135000",
                 "黑猫":"243000",
                 "飞扬":"175000"}
    if item in priceTable:
        return item+"的单价是："+priceTable[item]


agent = create_react_agent(
    model=ChatOllama(model="qwen2.5:7b",temperature = 0.8),
    tools=[getPriceByItem],
    response_format = PriceResponseList
)

prompt1 = "月光女神和黑猫这两款车多少钱？"
print("user:"+prompt1)
result = agent.invoke(
    {"messages": [{"role": "user", "content": prompt1}]}
)
print(result["structured_response"])