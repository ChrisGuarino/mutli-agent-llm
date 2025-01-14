from dotenv import load_dotenv
import os
import openai
import json

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def parse_command(command):
    """
    Uses LLM to parse the command and return the intent and action details.
    """
    prompt = f"Analyze the following command and output a structured action: '{command}'."+"Dictionary keys must be orangized into action, platform, and object."
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an assistant for parsing commands into structured actions."},
            {"role": "user", "content": prompt}
        ]
    )
    dict_response = json.loads(response["choices"][0]["message"]["content"])
    print(dict_response)
    return dict_response  

# #TEST 
# command = input("What do you want to do?")
# response = parse_command(command) 
# print(response)