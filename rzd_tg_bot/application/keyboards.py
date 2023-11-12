from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


main_kb = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text='Обучение'),
        KeyboardButton(text='Тестирование'),
    ],
    [KeyboardButton(text='Мой профиль')]
], resize_keyboard=True)


back_kb = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text='В главное меню')
    ]
], resize_keyboard=True)


education_kb = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text='В главное меню')
    ],
    [
        KeyboardButton(text='Очистить контекст и задать новый вопрос')
    ]
], resize_keyboard=True)


end_test_kb = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text='Завершить тестирование')
    ]
], resize_keyboard=True)


personal_account_kb = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Рейтинг', callback_data='with_rating')
    ]
])


personal_account_back_kb = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Назад', callback_data='back_to_personal_account')
    ]
])
