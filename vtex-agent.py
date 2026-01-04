import os
os.getenv('OPENAI_API_KEY')

from litellm import completion
import requests
from typing import List, Dict
import json

# Define a function to apply to each object
def getNameAndIdFromTemplate(template_obj):
    return {
        "name": template_obj['FriendlyName'], 
        "id": template_obj['Name']
    }

def getTemplateList():
    url = "https://jujacociunas.myvtex.com/api/template-render/pvt/templates/getlist"
    response = requests.get(url, headers = { "VtexIdclientAutCookie": "" })
    # Check the status code (200 indicates success)
    if response.status_code == 200:
        # print("Request successful!")
        templates = json.loads(response.text)
        simpleTemplates = list(map(getNameAndIdFromTemplate, templates))
        return simpleTemplates
    else:
        print("Request failed with status code: {response.status_code}")
        return None

def generate_response(messages: List[Dict]) -> str:
    """Call LLM to get response"""
    response = completion(
        model="openai/gpt-4o",
        messages=messages,
        max_tokens=1024
    )
    return response.choices[0].message.content

agent_rules = [
    {
        "role": "system", 
        "content": "You offer email templates customization services."
    }
]

user_messages = [
    {
        "role": "user", 
        "content": "List all available email templates and ask the user which one they want to customize."
    }
]


# print(response)

reponse2 = getTemplateList()
print(json.dumps(reponse2))

agent_rules = [
    {"role": "system", "content": "This is a list of email templates available for customization: " + json.dumps(reponse2)},
]

response = generate_response(agent_rules + user_messages)
print("Agent response: ", response)



# The Agent Loop
# while iterations < max_iterations:

#     # 1. Construct prompt: Combine agent rules with memory
#     prompt = agent_rules + memory

#     # 2. Generate response from LLM
#     print("Agent thinking...")
#     response = generate_response(prompt)
#     print(f"Agent response: {response}")

#     # 3. Parse response to determine action
#     action = parse_action(response)

#     result = "Action executed"

#     if action["tool_name"] == "list_files":
#         result = {"result":list_files()}
#     elif action["tool_name"] == "read_file":
#         result = {"result":read_file(action["args"]["file_name"])}
#     elif action["tool_name"] == "error":
#         result = {"error":action["args"]["message"]}
#     elif action["tool_name"] == "terminate":
#         print(action["args"]["message"])
#         break
#     else:
#         result = {"error":"Unknown action: "+action["tool_name"]}

#     print(f"Action result: {result}")

#     # 5. Update memory with response and results
#     memory.extend([
#         {"role": "assistant", "content": response},
#         {"role": "user", "content": json.dumps(result)}
#     ])

#     # 6. Check termination condition
#     if action["tool_name"] == "terminate":
#         break

#     iterations += 1