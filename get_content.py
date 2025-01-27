import pytesseract
from PIL import Image
from transformers import ViTFeatureExtractor, ViTForImageClassification
from PIL import Image

def extract_text_from_image(image_path):
    """
    Uses Tesseract OCR to extract text from an image.
    """
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    print("Extracted Text:")
    print(text)
    return text

def classify_image_elements(image_path):
    """
    Classifies elements in the image using a pre-trained Vision Transformer.
    """
    # Load pre-trained ViT model and feature extractor
    model_name = "google/vit-base-patch16-224"
    feature_extractor = ViTFeatureExtractor.from_pretrained(model_name)
    model = ViTForImageClassification.from_pretrained(model_name)

    # Load and preprocess the image
    image = Image.open(image_path)
    inputs = feature_extractor(images=image, return_tensors="pt")

    # Make predictions
    outputs = model(**inputs)
    logits = outputs.logits
    predicted_class = logits.argmax(-1).item()
    print(f"Predicted Class: {model.config.id2label[predicted_class]}")
