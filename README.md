# RZD-Virtual-Trainer   

Решение команды `Deviаnts` задачи "Виртуальный тренажер" от РЖД в рамках Хакатона [Цифровой прорыв](https://hacks-ai.ru).

Система обучения персонала РЖД, основанная на больших языковых моделях. Система может доступно и интересно объяснять материал, а также объективно оценивать знания.

Для поддержания мотивации к учёбе есть система поощрения.

Интерфейс решения представлен в виде чат-бота в Telegram.
## Стек решения
`Python`, `LLAMA 2`, `Hugging Face`, `LangChain`, `PyTorch`, `aiogram`

## [Ссылка на бота](https://t.me/rzd_employee_training_bot)
Запуск бота в dev-режиме
Перейти в директорию с ботом
```
cd rzd_tg_bot/
```
Cоздать и активировать виртуальное окружение:
```
python3 -m venv env
```
```
source env/bin/activate
```
Установить зависимости из файла requirements.txt:
```
python3 -m pip install --upgrade pip 
```
```
pip install -r requirements.txt
```
Запустить файл `run.py`


## Файлы  
[`server.ipynb`](server.ipynb) — хостинг API на Colab (работает на Tesla T4)

[`make_submit.ipynb`](make_submit.ipynb) — получение сабмита

[`rzd_tg_bot/`](rzd_bot/) — директория с ботом 
