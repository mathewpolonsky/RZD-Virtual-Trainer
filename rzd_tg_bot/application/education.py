from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from .keyboards import back_kb, education_kb
from .states import Education
from .api_requests import get_answer

ed_router = Router()

start_history = {'role': 'system',
                 'content': 'Используй следующие фрагменты контекста, чтобы ответить на вопрос в конце. Если ты не знаешь ответа, просто скажи, что не знаешь что ответить, не пытайся придумать ответ'}


@ed_router.message(F.text == "Обучение")
async def education(message: Message, state: FSMContext) -> None:
    await message.answer("Задайте свой вопрос", reply_markup=back_kb)
    await state.set_state(Education.waiting_for_question)
    history = [start_history]
    await state.update_data(history=history)


@ed_router.message(Education.waiting_for_question)
async def answer_question(message: Message, state: FSMContext) -> None:
    if message.text == "Очистить контекст и задать новый вопрос":
        await message.answer("Задайте свой вопрос", reply_markup=back_kb)
        await state.update_data(history=[start_history])
    else:
        data = await state.get_data()
        history = data.get("history", [])
        await message.answer("⏳")
        history.append({"role": "user", "content": message.text})
        answer = await get_answer(history)
        history.append({"role": "bot", "content": answer})
        print(history)
        await message.answer(answer)
        await message.answer("Задайте следующий вопрос", reply_markup=education_kb)
