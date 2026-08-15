from typing_extensions import TypedDict
from typing import Annotated
import operator

def custom_reducer(left, right):
    return left + right

class State(TypedDict):
    count: Annotated[int, operator.add]
    tags: Annotated[list, custom_reducer]

state: State = {"count": 1, "tags": ["a"]}
print(state)
