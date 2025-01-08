def dispatch_command(command):
    """
    Directs the command to the appropriate agent based on intent.
    """
    if "open" in command or "application" in command:
        return "Application Agent"
    elif "search" in command or "navigate" in command:
        return "Web Navigation Agent"
    elif "note" in command or "reminder" in command:
        return "Task Manager Agent"
    elif "organize" in command or "file" in command:
        return "File Manager Agent"
    elif "schedule" in command:
        return "Scheduler Agent"
    else:
        return "Error Handler Agent"
