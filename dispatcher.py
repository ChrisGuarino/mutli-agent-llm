from command_functions import navigate_and_extract,add_comment

def dispatch_command(parsed_command):
    """
    Executes an action based on the parsed command.
    """
    intent = parsed_command["intent"]
    parameters = parsed_command["parameters"]

    if intent == "add_comment":
        step = parameters["step"]
        comment = parameters["comment"]
        print(f"Adding comment '{comment}' to step {step}.")
        # Call a function to add the comment on the website
        add_comment(step,comment)

    elif intent == "navigate":
        direction = parameters["direction"]
        print(f"Navigating {direction}.")
        # Call a function to navigate (e.g., next/previous step)
        step = parameters["step"]
        navigate_and_extract(step)

    elif intent == "retrieve_info":
        step = parameters["step"]
        print(f"Retrieving information for step {step}.")
        # Call a function to retrieve step details

    elif intent == "update_status":
        step = parameters["step"]
        status = parameters["status"]
        print(f"Updating status of step {step} to '{status}'.")
        # Call a function to update step status

    else:
        print("Unknown intent.")
