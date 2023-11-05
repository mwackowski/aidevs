import json
import sys

sys.path.append("..")

from common.aidevs_authorize import get_task, get_token, send_answer
from common.openai_requests import send_chat_completion


task_name = "blogger"
token = get_token(task_name)
task = get_task(token)

print(task["msg"])
print("\n".join(task["blog"]))

# r = send_chat_completion(
#     model_version="gpt-4",
#     system_content="""you are a pizza man that writes a blog, provide me information only with regards to pizza on prompt.\n
#     You will be provided with 4 lines representing chapters and I want you to write a few more words to extend the topic for each of them.
#     Your answers should be in a JSON format with chapter as keys and your answer as values""",
#     user_content="\n".join(task["blog"]),
#     temperature=0.3,
# )

r = send_chat_completion(
    model_version="gpt-4",
    system_content="""You will be provided with 4 lines representing chapters and I want you to extend the topic for each of them.
    Your answers should be in a JSON format with chapter as keys and your answer as values""",
    user_content="\n".join(task["blog"]),
    temperature=0.3,
)

resp = json.loads(r["choices"][0]["message"]["content"])
answer = [f"{k}: {v}" for k, v in resp.items()]
resp_answer = send_answer(token=token, answer=answer)
