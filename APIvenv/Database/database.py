from sqlalchemy import PickleType ,MetaData,Table,Column,  Integer, String
from pydantic import BaseModel
from typing import List

metadata = MetaData()
class TextSpace(BaseModel):
    question: str
    ansver: str

class Radio(BaseModel):
    question: str
    variants: List[str]
    ansver: int

class CheckBox(BaseModel):
    question: str
    variants: List[str]
    ansver: List[int]
class Form(BaseModel):
    Creator: str
    TextSpaces: List[TextSpace]
    Radios: List[Radio]
    CheckBoxes: List[CheckBox]



Forms = Table(
    "Forms",
    metadata,
    Column("Form", PickleType)
)

