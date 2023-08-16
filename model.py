from pydantic import BaseModel

class ToDo(BaseModel):
    id: int
    title: str
    description: str
    done: bool
