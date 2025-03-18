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
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an assistant for a project-tracking tool. "
                    "Your job is to parse natural language commands into structured JSON instructions. "
                    "These commands may involve navigating steps, adding comments, retrieving information, "
                    "or updating step statuses on a website. Always return the parsed intent and parameters in JSON format."
                )
            },
            {
                "role": "user",
                "content": (
                    f"Parse the following command: {command}\n"
                    "Provide the output in JSON format with an 'intent' and 'parameters' field. "
                    "For example:\n"
                    "{\n"
                    '  "intent": "add_comment",\n'
                    '  "parameters": {"step": 46, "comment": "This process is complete"}\n'
                    "}"
                )
            }
        ]
    )

    parsed_response = response["choices"][0]["message"]["content"]
    return json.loads(parsed_response)

# TEST
command = input("What do you want to do? ")
response = parse_command(command)
print(response)
