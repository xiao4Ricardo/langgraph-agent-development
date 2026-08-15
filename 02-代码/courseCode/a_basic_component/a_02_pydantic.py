from pydantic import BaseModel, Field, EmailStr

class User(BaseModel):
    id: int
    name: str = "张三"
    email: EmailStr
    age: int = Field(gt=0, le=150)  # 年龄必须 >0 且 <=150

user = User(id=1, email="zhangsan@example.com", age=25)
print(user)
