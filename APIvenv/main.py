from fastapi import FastAPI, Depends,  HTTPException
from pydantic import BaseModel
from typing import List
from Session import get_async_session
from sqlalchemy import insert, select, text
from sqlalchemy.ext.asyncio import AsyncSession
from Database.database import Forms
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
app = FastAPI(
    title = "Forms"
)


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
class Formss(BaseModel):
    Form: Form

a = []
@app.post("/add_form", summary=" Запрос на отправку формы, состоящий из имени создателя, и трех списков, в которых находяться поля для ответов на вопросы, радио кнопки и чекбоксы.")
async def add_form( new_form: Formss, session: AsyncSession = Depends(get_async_session)):
    query = insert(Forms).values(new_form.dict())
    await session.execute(query)
    await session.commit()
    return {"status": "success"}

