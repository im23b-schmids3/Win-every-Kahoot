import easyocr
from PIL import ImageGrab
import pygetwindow
import os
from dotenv import load_dotenv
import groq

# Load API key from .env file
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

# Initialize Groq client
client = groq.Client(api_key=groq_api_key)

# Get Kahoot window
Kahoot_window = pygetwindow.getWindowsWithTitle("Google Chrome")
if Kahoot_window:
    kahoot = Kahoot_window[0]
    kahoot.activate()

# Define screenshot areas
question_box = (25, 250, 2800, 400)  # Question area
answer1_box = (25, 1200, 1200, 1500)  # Answer 1
answer2_box = (1150, 1200, 2420, 1500)  # Answer 2
answer3_box = (25, 1600, 1210, 1800)  # Answer 3
answer4_box = (1150, 1600, 2420, 1800)  # Answer 4

# Take screenshots
ImageGrab.grab(bbox=question_box).save("question.png")
ImageGrab.grab(bbox=answer1_box).save("answer1.png")
ImageGrab.grab(bbox=answer2_box).save("answer2.png")
ImageGrab.grab(bbox=answer3_box).save("answer3.png")
ImageGrab.grab(bbox=answer4_box).save("answer4.png")

# Initialize EasyOCR
reader = easyocr.Reader(['en', 'de', 'fr'])

# OCR Processing
images = ["question.png", "answer1.png", "answer2.png", "answer3.png", "answer4.png"]
labels = ["Question", "Answer 1", "Answer 2", "Answer 3", "Answer 4"]

extracted_text = {}

for img, label in zip(images, labels):
    result = reader.readtext(img)
    text_content = " ".join([text for (_, text, _) in result])
    extracted_text[label] = text_content
    print(f"\n{label}: {text_content}")

# Ensure all text is extracted
if "Question" in extracted_text and all(f"Answer {i}" in extracted_text for i in range(1, 5)):
    question = extracted_text["Question"]
    answers = [extracted_text[f"Answer {i}"] for i in range(1, 5)]

    # Format the prompt for Groq AI
    prompt = f"""
    You are playing Kahoot. The question is: "{question}".
    The possible answers are:
    1. {answers[0]}
    2. {answers[1]}
    3. {answers[2]}
    4. {answers[3]}

    Which answer is most likely correct? Respond with ONLY the answer number (1-4).
    """

    response = client.chat.completions.create(
        model="mixtral-8x7b-32768",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=50
    )

    # Extract AI response
    ai_response = response.choices[0].message.content.strip()
    print(f"\n Best Answer: {ai_response}")
else:
    print("\n Error: Could not extract question or answers properly.")
