import subprocess

def execute_action(action_dict):
    """
    Executes an action based on a structured dictionary input.
    
    Example dictionary format:
    {
        "action": "search",
        "platform": "amazon",
        "object": "toy"
    }
    """
    action = action_dict.get("action", "").lower()
    platform = action_dict.get("platform", "").lower()
    obj = action_dict.get("object", "").strip()

    if action == "search":
        if platform == "amazon":
            if obj:
                try:
                    url = f"https://www.amazon.com/s?k={obj}"
                    subprocess.run(["open", url])  # macOS
                    print(f"Searched on Amazon for: {obj}")
                except Exception as e:
                    print(f"Error searching on Amazon: {e}")
            else:
                print("Error: 'object' to search is missing.")
        elif platform == "google":
            if obj:
                try:
                    url = f"https://www.google.com/search?q={obj}"
                    subprocess.run(["open", url])  # macOS
                    print(f"Searched on Google for: {obj}")
                except Exception as e:
                    print(f"Error searching on Google: {e}")
            else:
                print("Error: 'object' to search is missing.")
        else:
            print(f"Error: Platform '{platform}' is not supported for search.")
    
    elif action == "open application":
        app_name = action_dict.get("object", "").strip()
        if app_name:
            try:
                subprocess.Popen(["open", "-a", app_name])  # macOS
                print(f"Opened application: {app_name}")
            except Exception as e:
                print(f"Error opening application {app_name}: {e}")
        else:
            print("Error: 'object' (application name) is missing.")
    
    else:
        print(f"Action '{action}' not recognized.")