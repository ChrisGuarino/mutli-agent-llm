from playwright.sync_api import sync_playwright

# def run(playwright):
#     chrome_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
#     browser = playwright.chromium.launch(headless=False, executable_path=chrome_path)
#     page = browser.new_page()
#     page.goto("https://login.w3.ibm.com/authsvc/mtfim/sps/authsvc?PolicyId=urn:ibm:security:authentication:asf:onpremldap&identity_source_id=7fdde1e3-ba89-44ab-820b-275718128bb4&Target=https%3A%2F%2Flogin.w3.ibm.com%2Fsaml%2Fsps%2Fauth")

#     page.fill("input[name='username']", "Christopher.Guarino1@ibm.com")
#     page.fill("input[name='password']", "ibmPleaseloginnow{")
#     page.click("button[type='submit']")

#     # Take a screenshot
#     # page.screenshot(path="screenshot.png")
#     # browser.close()
#     print("Browser will remain open. You can manually close it when done.")
#     try:
#         while True:
#             pass  # Infinite loop to prevent the script from exiting
#     except KeyboardInterrupt:
#         print("Exiting script...")
#         browser.close()  # Manually close the browser when script is stopped
#         playwright.stop()

# with sync_playwright() as playwright:
#     run(playwright)


#May want
# def run_with_persistent_context(playwright):
#     # Specify Chrome path
#     chrome_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

#     # Launch Chrome with a persistent context
#     browser = playwright.chromium.launch_persistent_context(
#         user_data_dir="user_data",  # Directory to save session data
#         headless=False,
#         executable_path=chrome_path
#     )
#     page = browser.pages[0] if browser.pages else browser.new_page()

#     # Navigate to a website
#     page.goto("https://login.w3.ibm.com/authsvc/mtfim/sps/authsvc?PolicyId=urn:ibm:security:authentication:asf:onpremldap&identity_source_id=7fdde1e3-ba89-44ab-820b-275718128bb4&Target=https%3A%2F%2Flogin.w3.ibm.com%2Fsaml%2Fsps%2Fauth")

#     page.fill("input[name='username']", "Christopher.Guarino1@ibm.com")
#     page.fill("input[name='password']", "ibmPleaseloginnow{")
#     page.click("button[type='submit']")
#     # # Close the browser
#     # browser.close()

# with sync_playwright() as playwright:
#     run_with_persistent_context(playwright)

# def navigate_and_extract(step_number):
#     with sync_playwright() as playwright:
#         # Launch browser
#         browser = playwright.chromium.launch(headless=False)  # Use headless=True for faster automation without UI
#         page = browser.new_page()

#         # Navigate to the project-tracking website
#         page.goto("https://watkmrl1.watson.ibm.com/mrltrack/")

#         # Navigate to the specific step
#         step_input_selector = "input[name='step_input']"  # Replace with actual input field selector for step navigation
#         page.fill(step_input_selector, str(step_number))
#         page.press(step_input_selector, "Enter")

#         # Extract details from the step
#         process = page.locator("span#process_id").inner_text()  # Replace with actual selector for process
#         comments = page.locator("div#comments_section").inner_text()  # Replace with actual selector for comments
#         status = page.locator("span#status").inner_text()  # Replace with actual selector for status

#         # Print or return the extracted details
#         print(f"Step {step_number} Details:")
#         print(f"Process: {process}")
#         print(f"Comments: {comments}")
#         print(f"Status: {status}")

#         # Close the browser
#         browser.close()

# def add_comment(step_number, comment):
#     with sync_playwright() as playwright:
#         browser = playwright.chromium.launch(headless=False)
#         page = browser.new_page()

#         # Navigate and login (similar to the above example)

#         # Navigate to the specific step
#         page.fill("input[name='step_input']", str(step_number))
#         page.press("input[name='step_input']", "Enter")

#         # Add comment
#         comment_box_selector = "textarea#comment_box"  # Replace with actual selector
#         page.fill(comment_box_selector, comment)
#         page.click("button#save_comment")  # Replace with actual selector for save button

#         print(f"Added comment '{comment}' to step {step_number}.")
#         browser.close() 

# def update_status(step_number, status):
#     with sync_playwright() as playwright:
#         browser = playwright.chromium.launch(headless=False)
#         page = browser.new_page()

#         # Navigate and login (similar to the above example)

#         # Navigate to the specific step
#         page.fill("input[name='step_input']", str(step_number))
#         page.press("input[name='step_input']", "Enter")

#         # Update status
#         status_dropdown_selector = "select#status_dropdown"  # Replace with actual selector
#         page.select_option(status_dropdown_selector, status)
#         page.click("button#save_status")  # Replace with actual selector for save button

#         print(f"Updated status of step {step_number} to '{status}'.")
#         browser.close()

# def execute_command(parsed_command):
#     intent = parsed_command["intent"]
#     parameters = parsed_command["parameters"]

#     if intent == "retrieve_info":
#         step = parameters["step"]
#         navigate_and_extract(step)
#     elif intent == "add_comment":
#         step = parameters["step"]
#         comment = parameters["comment"]
#         add_comment(step, comment)
#     elif intent == "update_status":
#         step = parameters["step"]
#         status = parameters["status"]
#         update_status(step, status)
#     else:
#         print("Unknown intent.")
