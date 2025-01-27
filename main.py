from window_tools import monitor_active_window
from get_content import extract_text_from_image, classify_image_elements
def main():

    monitor_active_window()
    img_text = extract_text_from_image(image_path='/Users/chrisguarino/Documents/Programming/mutli-agent-llm/images/active_window.png')
    print(img_text)
    img_annotations = classify_image_elements(image_path='/Users/chrisguarino/Documents/Programming/mutli-agent-llm/images/active_window.png')
    img_annotations
    
if __name__ == "__main__":
    main() 
