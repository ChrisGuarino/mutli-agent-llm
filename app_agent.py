import subprocess
from field_reasoning import reason

def application_agent(dict):
    """
    Handles application-related tasks.
    """
    command = dict['action']
    print(dict)

    if "open" in command.lower():
        app_name = dict['application']
        std_app_name = reason(app_name)
        try:
            subprocess.Popen(["open", "-a", std_app_name])  # macOS
            return f"Opened {std_app_name}."
        except Exception as e:
            return f"Error: Could not open {std_app_name}. Details: {e}"
    else:
        return "Command not recognized by Application Agent."
