from typing_extensions import TypedDict

class Person(TypedDict):
    name: str
    age: int

person: Person = {"name": "Alice", "age": 30}
print(person)
