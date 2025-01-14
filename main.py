from command_parsing import parse_command
from dispatcher import dispatch_command 
from app_agent import application_agent
from webnav_agent import web_navigation_agent

def main():
    while True:
        user_input = input("What would you like to do? ")
        input_dict = parse_command(user_input)
        action = input_dict['action']
        if action.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        agent = dispatch_command(action)
        print(f"Dispatching to: {agent}")

        if agent == "Application Agent":
            result = application_agent(input_dict)
        elif agent == "Web Navigation Agent":
            result = web_navigation_agent(input_dict)
        else:
            result = "Agent not implemented yet."

        print(result)

if __name__ == "__main__":
    main() 




