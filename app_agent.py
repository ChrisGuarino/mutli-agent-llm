import subprocess

def application_agent(command):
    """
    Handles application-related tasks.
    """
    if "open" in command.lower():
        app_name = command.split("open")[-1].strip()
        try:
            subprocess.Popen(["open", "-a", app_name])  # macOS
            return f"Opened {app_name}."
        except Exception as e:
            return f"Error: Could not open {app_name}. Details: {e}"
    else:
        return "Command not recognized by Application Agent."
