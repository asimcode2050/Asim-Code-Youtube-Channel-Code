from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

def text_from_image(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text

if __name__ == "__main__":
    image_path = "Hello_World_in_Python.png"
    extracted_text = text_from_image(image_path)
    print('Extracted Text:')
    print(extracted_text)
