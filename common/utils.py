def get_message(ai_response):
    """Return a message from ai response.

    Exemplary response to retrieve message from:
    {'id': 'chatcmpl-8GDWNsy3CKLCdKBYpt9P8dEizzU0x',
    'object': 'chat.completion',
    'created': 1698875915,
    'model': 'gpt-4-0613',
    'choices': [{'index': 0,
    'message': {'role': 'assistant', 'content': 'Alojzy'},
    'finish_reason': 'stop'}],
    'usage': {'prompt_tokens': 75, 'completion_tokens': 4, 'total_tokens': 79}}
    """
    return ai_response["choices"][0]["message"]["content"]
