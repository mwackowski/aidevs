import json
import requests

from common._secrets import AIDEVS_KEY


BASE_URL = "https://zadania.aidevs.pl/"
DATA = {"apikey": AIDEVS_KEY}


def get_token(task: str):
    resp = requests.post(f"{BASE_URL}/token/{task}", data=json.dumps(DATA))
    resp.raise_for_status()
    return json.loads(resp.text)["token"]


def get_task(token: str) -> str:
    resp = requests.get(f"{BASE_URL}/task/{token}")
    return json.loads(resp.text)


def send_answer(token: str, answer: str) -> str:
    resp = requests.post(
        f"{BASE_URL}/answer/{token}", data=json.dumps({"answer": answer})
    )
    return resp.text
