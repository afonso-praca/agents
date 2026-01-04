import os
os.environ['OPENAI_API_KEY'] = ""

from litellm import completion
from typing import List, Dict


def generate_response(messages: List[Dict]) -> str:
    """Call LLM to get response"""
    response = completion(
        model="openai/gpt-4o",
        messages=messages,
        max_tokens=1024
    )
    return response.choices[0].message.content


messages = [
    {"role": "system", "content": "You are digital commerce expert, skilled in providing solutions for online businesses."},
    {"role": "user", "content": "If composing an ecommerce solutions architecture, what are the key components to consider?"}
]

response = generate_response(messages)
print(response)