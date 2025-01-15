from dotenv import load_dotenv
import os
import openai
import json
from field_reasoning import reason

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def parse_command(command):
    """
    Uses LLM to parse the command and return the intent and action details.
    """
    prompt = f"Analyze the following command and output a structured action: '{command}'."+"Dictionary keys must be orangized into action, website, application, and (if applicable) object."
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an assistant for parsing commands from the user into a dictionary of values to be executed by other agents. Commands pretain to opening an application locally, searching a website, starting a note, setting a reminder, etc."},
            {"role": "user", "content": prompt}
        ]
    )
    dict_response = json.loads(response["choices"][0]["message"]["content"])
    new_dict = {key: reason(value) for key, value in dict_response.items()}
    print (f'Original Dict: {dict_response}\nNew Dict: {new_dict}') 
    return new_dict 

#TEST 
command = input("What do you want to do?")
response = parse_command(command) 
print(response)