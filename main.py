import easyocr
from PIL import ImageGrab

reader = easyocr.Reader(['en', 'de', 'fr'])  # Can read text in English, German and French

screenshot = ImageGrab.grab()   # Takes a screenshot of the screen
screenshot.save("screenshot1.png")  # Saves the screenshot to a file
result = reader.readtext("screenshot1.png")  # Reads the text in the file
screenshot.close()  # Closes the screenshot

for (bbox, text, prob) in result:
    print(f'Text: {text}, Probability: {prob}')

