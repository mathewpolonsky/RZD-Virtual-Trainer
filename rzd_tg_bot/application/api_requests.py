import asyncio
import aiohttp

from typing import List, Tuple, Dict

async def get_answer(context: List[Dict[str, str]]) -> str:
    api_url = "https://patient-buck-weekly.ngrok-free.app/get_answer"
    payload = {
        "context": context
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(api_url, json=payload) as response:
            answer = await response.json()
            return answer


async def get_rand_question() -> Tuple[str, str]:
    api_url = "https://patient-buck-weekly.ngrok-free.app/get_rand_question"
    async with aiohttp.ClientSession() as session:
        async with session.get(api_url) as response:
            response_json = await response.json()
            question_id = response_json["question_id"]
            question = response_json["question"]
            return question_id, question


async def check_answer(question_id: str, answer: str) -> Tuple[float, str]:
    api_url = "https://patient-buck-weekly.ngrok-free.app/check_answer"
    payload = {
        "question_id": question_id,
        "answer": answer,
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(api_url, json=payload) as response:
            response_json = await response.json()
            return response_json["answer_coef"], response_json["expected_answer"]
