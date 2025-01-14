import subprocess

def application_agent(dict):
    """
    Handles application-related tasks.
    """
    command = dict['action']
    if "open" in command.lower():
        app_name = dict['platform']
        try:
            subprocess.Popen(["open", "-a", app_name])  # macOS
            return f"Opened {app_name}."
        except Exception as e:
            return f"Error: Could not open {app_name}. Details: {e}"
    else:
        return "Command not recognized by Application Agent."
