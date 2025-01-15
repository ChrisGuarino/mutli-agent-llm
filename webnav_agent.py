import webbrowser

def web_navigation_agent(dict):
    """
    Handles web navigation tasks.
    """

    command = dict['action']
    print(dict)
    if "search" in command.lower():
        query = dict['object']
        url = f"https://www.google.com/search?q={query}"
        webbrowser.open(url)
        return f"Searched Google for: {query}"
    else:
        return "Command not recognized by Web Navigation Agent."
