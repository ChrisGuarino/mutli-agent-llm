import webbrowser

def web_navigation_agent(command):
    """
    Handles web navigation tasks.
    """
    if "search" in command.lower():
        query = command.split("search")[-1].strip()
        url = f"https://www.google.com/search?q={query}"
        webbrowser.open(url)
        return f"Searched Google for: {query}"
    else:
        return "Command not recognized by Web Navigation Agent."
