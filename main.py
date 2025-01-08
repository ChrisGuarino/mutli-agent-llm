from dispatcher import dispatch_command 
from app_agent import application_agent
from webnav_agent import web_navigation_agent

def main():
    while True:
        user_input = input("What would you like to do? ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        agent = dispatch_command(user_input)
        print(f"Dispatching to: {agent}")

        if agent == "Application Agent":
            result = application_agent(user_input)
        elif agent == "Web Navigation Agent":
            result = web_navigation_agent(user_input)
        else:
            result = "Agent not implemented yet."

        print(result)

if __name__ == "__main__":
    main() 




