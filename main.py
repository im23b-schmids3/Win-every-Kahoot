import easyocr
from PIL import ImageGrab
import pygetwindow

Kahoot_window = pygetwindow.getWindowsWithTitle("Google Chrome")  # Gets the window with the title 'Google Chrome'
if Kahoot_window:
    kahoot = Kahoot_window[0]
    kahoot.activate()

question_box = (25, 250, 2800, 400)  # Question area
answer1_box = (25, 1200, 1200, 1500)  # Answer 1
answer2_box = (1000, 1200, 2420, 1500)  # Answer 2
answer3_box = (25, 1600, 1210, 1800)  # Answer 3
answer4_box = (1000, 1600, 2420, 1800)  # Answer 4

# Take screenshots
ImageGrab.grab(bbox=question_box).save("question.png")
ImageGrab.grab(bbox=answer1_box).save("answer1.png")
ImageGrab.grab(bbox=answer2_box).save("answer2.png")
ImageGrab.grab(bbox=answer3_box).save("answer3.png")
ImageGrab.grab(bbox=answer4_box).save("answer4.png")

print("Screenshots saved!")


reader = easyocr.Reader(['en', 'de', 'fr'])  # Can read text in English, German and French


images = ["question.png", "answer1.png", "answer2.png", "answer3.png", "answer4.png"]
labels = ["Question", "Answer 1", "Answer 2", "Answer 3", "Answer 4"]

for img, label in zip(images, labels):
    result = reader.readtext(img)
    print(f"\n{label}:")
    for (bbox, text, prob) in result:
        print(f'  Text: {text}, Probability: {prob:.2f}')
