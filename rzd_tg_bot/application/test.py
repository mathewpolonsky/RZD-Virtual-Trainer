from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from .keyboards import end_test_kb, main_kb
from .states import Test
from database.requests import increase_score
from .api_requests import get_rand_question, check_answer

test_router = Router()


@test_router.message(F.text == "Завершить тестирование")
async def end_test(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    await message.answer(f"Вы завершили тестирование, набрав {data.get('counter')} баллов", reply_markup=main_kb)
    await state.clear()


@test_router.message(F.text == "Тестирование")
async def test(message: Message, state: FSMContext) -> None:
    await state.set_state(Test.Q1)
    await message.answer("Вопрос загружается...", reply_markup=end_test_kb)
    question_id, question = await get_rand_question()
    await state.update_data(question_id=question_id)
    counter = 0
    await state.update_data(counter=counter)
    await message.answer(f"Вопрос {question_id}: {question}", reply_markup=end_test_kb)


@test_router.message(Test.Q1)
async def question_1(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    question_id = data.get("question_id")
    answer_correctness_coef, expected_answer = await check_answer(question_id, message.text)
    if answer_correctness_coef > 0.75:
        await message.answer("Правильно! +1 балл")
        await increase_score(message.from_user.id)
        await state.update_data(counter=data.get("counter") + 1)
    else:
        await message.answer(f"Неправильно!\nПравильный ответ: {expected_answer}")
    new_question_id, new_question = await get_rand_question()
    await state.update_data(question_id=new_question_id)
    await message.answer("Следующий вопрос...", reply_markup=end_test_kb)
    await message.answer(f"Вопрос {new_question_id}: {new_question}", reply_markup=end_test_kb)
