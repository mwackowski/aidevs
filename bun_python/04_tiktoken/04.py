from count_tokens import count_tokens
from tiktoken import get_encoding


class Message:
    def __init__(self, role: str, content: str, name: str = None):
        self.role = role
        self.content = content
        self.name = name


messages = [Message(role="system", content="Hey, you!")]

num = count_tokens(messages, "gpt-4")
print("Token Count: ", num)
encoding = get_encoding("cl100k_base")
print("Token IDs: ", encoding.encode(messages[0].content))
