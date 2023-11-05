import json
import requests
import sys

sys.path.append("..")

from common.aidevs_authorize import get_task, get_token, send_answer, BASE_URL
from common.openai_requests import send_moderations, send_chat_completion

task_name = "liar"
token = get_token(task_name)
task = get_task(token)

question = "what is capital of Poland? Answer ultra-briefly, possibly in one word."
resp = requests.post(f"{BASE_URL}/task/{token}", data={"question": question})
liar_answer = json.loads(resp.text)["answer"]

resp_gpt = send_chat_completion(
    model_version="gpt-4",
    system_content="Provide brief Yes/No answer",
    user_content=f"""You will be provided with a question and answer. Tell if the answer is correct or not.\n
    ###Question: {question}\n
    ###Answer: {liar_answer}""",
)

guard_rail = resp_gpt["choices"][0]["message"]["content"]

resp_after_guard = send_answer(token, guard_rail)
print(json.loads(resp_after_guard))
