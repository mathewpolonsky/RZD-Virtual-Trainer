from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from .keyboards import main_kb, personal_account_kb
from database.requests import add_user_if_not_exists, get_user, get_user_rank, get_top_users
from appearance.emojis_statuses import get_status

main_router = Router()


@main_router.message(CommandStart())
async def command_start(message: Message) -> None:
    await add_user_if_not_exists(message.from_user.id, message.from_user.full_name)
    await message.answer(
        "Здравствуйте! Добро пожаловать в бота для обучения и тестирования сотрудников РЖД!",
        reply_markup=main_kb,
    )


@main_router.message(F.text == "В главное меню")
async def go_back(message: Message, state: FSMContext) -> None:
    await state.clear()
    await message.answer("Вы вернулись назад.", reply_markup=main_kb)


@main_router.message(F.text == "Мой профиль")
async def my_profile(message: Message) -> None:
    user = await get_user(message.from_user.id)
    text = f"Ваш профиль:\n" \
           f"Имя: {user.name}\n" \
           f"Статус: {get_status(user.score)}\n" \
           f"Баллы: {user.score}\n" \
           f"Место в рейтинге: {await get_user_rank(message.from_user.id)}"
    await message.answer(text, reply_markup=personal_account_kb)


@main_router.callback_query(F.data == "with_rating")
async def top_10(callback: CallbackQuery) -> None:
    top_users = await get_top_users()
    text = "Десятка лучших железнодорожников:\n"
    for i, user in enumerate(top_users, start=1):
        text += f"{i}. {user.name} {get_status(user.score)} - {user.score}\n"
    await callback.bot.edit_message_text(chat_id=callback.message.chat.id,
                                         message_id=callback.message.message_id, text=text,
                                         )
    await callback.answer()
