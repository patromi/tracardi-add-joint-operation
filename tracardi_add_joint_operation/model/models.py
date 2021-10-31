from pydantic import BaseModel


class Module(BaseModel):
    join_string: str
    array : str
