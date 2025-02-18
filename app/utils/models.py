from pydantic import BaseModel


class StringTypeRequest(BaseModel):
    value: str

class FloatTypeRequest(BaseModel):
    value: float

class BooleanTypeRequest(BaseModel):
    value: bool