from pydantic import BaseModel


class StringTypeRequest(BaseModel):
    value: str

    @property
    def datatype(self):
        return str


class FloatTypeRequest(BaseModel):
    value: float

    @property
    def datatype(self):
        return float


