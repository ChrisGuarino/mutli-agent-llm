import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
############################################################
import time
from PIL import ImageGrab
import Quartz

def get_active_window_geometry():
    """
    Retrieves the title and geometry of the most prominent active window on macOS.
    """
    window_list = Quartz.CGWindowListCopyWindowInfo(
        Quartz.kCGWindowListOptionOnScreenOnly | Quartz.kCGWindowListOptionIncludingWindow,
        Quartz.kCGNullWindowID
    )

    for window in window_list:
        if window.get('kCGWindowName') and window.get('kCGWindowBounds'):
            # Only consider windows with valid bounds and titles
            bounds = window['kCGWindowBounds']
            title = window['kCGWindowName']
            left, top, width, height = bounds['X'], bounds['Y'], bounds['Width'], bounds['Height']

            # Filter out very small dimensions (likely icons or toolbars)
            if width > 100 and height > 100:
                return title, (int(left), int(top), int(left + width), int(top + height))

    return None, None

def capture_active_window(geometry):
    """
    Captures a screenshot of the active window based on its geometry.
    """
    if not geometry:
        print("No geometry provided for the active window.")
        return None

    # Unpack geometry
    left, top, right, bottom = geometry
    print(f"Geometry reported: {geometry}")


    # Capture the region
    # screenshot = ImageGrab.grab(bbox=(left, top, right, bottom))
    # timestamp = int(time.time())
    # screenshot.save(f"images/active_window_{timestamp}.png")
    # print(f"Screenshot saved as 'active_window_{timestamp}.png'.")
    # return screenshot

    screenshot = ImageGrab.grab(bbox=(left, top, right, bottom))
    screenshot.save(f"images/active_window.png")
    print(f"Screenshot saved as 'active_window.png'.")
    return screenshot


def monitor_active_window():
    """
    Continuously monitors the active window for changes in title or geometry.
    """
    previous_title = None
    previous_geometry = None

    print("Monitoring active window... Press Ctrl+C to stop.")
    try:
        while True:
            # Get the current active window's title and geometry
            current_title, current_geometry = get_active_window_geometry()

            # Check if the active window has changed
            if current_title != previous_title or current_geometry != previous_geometry:
                print(f"\nActive Window Changed: {current_title}")
                print(f"Geometry: {current_geometry}")

                # Capture the new active window
                if current_geometry:
                    capture_active_window(current_geometry)

                # Update the previous title and geometry
                previous_title = current_title
                previous_geometry = current_geometry

            # Wait before checking again
            time.sleep(1)  # Adjust the interval as needed (1 second here)

    except KeyboardInterrupt:
        print("\nStopped monitoring the active window.")


if __name__ == "__main__":
    monitor_active_window()
