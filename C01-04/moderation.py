import json
import sys

sys.path.append("..")

from common.aidevs_authorize import get_task, get_token, send_answer
from common.openai_requests import send_moderations


token = get_token("moderation")
task = get_task(token)

print(task["msg"])

moderations = []
for input in task["input"]:
    print(f"Sending moderation for: {input}")
    resp_moderations = send_moderations(input)
    moderations.append(resp_moderations)

answer = [int(m["results"][0]["flagged"]) for m in moderations]
resp_answer = send_answer(token=token, answer=answer)
