from dotenv import load_dotenv
import os
import openai

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def reason(command):
   
    prompt = f"Analyze the following string and output a known application, website, platform, etc. {command} Return only the name of the application, website, platform, or simply correct the spelling."
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an assistant to error correct user input. You need to take a colloquial or mispelled input and output best guess of what the user meant. If a value is an empty string just leave it."},
            {"role": "user", "content": prompt}
        ]
    )
    response = response["choices"][0]["message"]["content"]
    return response  

# #TEST 
# command = input("What do you want to do?")
# response = reason(command) 
# print(response)