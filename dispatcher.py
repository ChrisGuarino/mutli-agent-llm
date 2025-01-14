def dispatch_command(command):
    """
    Directs the command to the appropriate agent based on intent.
    """
    lc_command = command.lower()
    if "open" in lc_command or "application" in lc_command:
        return "Application Agent"
    elif "search" in lc_command or "navigate" in lc_command:
        return "Web Navigation Agent"
    elif "note" in lc_command or "reminder" in lc_command:
        return "Task Manager Agent"
    elif "organize" in lc_command or "file" in lc_command:
        return "File Manager Agent"
    elif "schedule" in lc_command:
        return "Scheduler Agent"
    else:
        return "Error Handler Agent"
