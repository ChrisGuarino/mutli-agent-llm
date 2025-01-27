import pyautogui

def perform_action(action, coordinates, text=None):
    """
    Performs an action (click or type) at specified coordinates.
    """
    if action == "click":
        pyautogui.click(x=coordinates[0], y=coordinates[1])
    elif action == "type":
        pyautogui.click(x=coordinates[0], y=coordinates[1])  # Focus the input
        pyautogui.typewrite(text, interval=0.1)
