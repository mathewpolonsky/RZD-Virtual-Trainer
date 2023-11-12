from aiogram.fsm.state import State, StatesGroup

class MainMenu(StatesGroup):
    education_block = State()
    test_block = State()


class Test(StatesGroup):
    Q1 = State()
    Q2 = State()
    Q3 = State()


class Education(StatesGroup):
    waiting_for_answer = State()
    waiting_for_question = State()
