import os
import groq
import keyboard
import requests
from PIL import ImageGrab
from dotenv import load_dotenv


def take_screenshots():
    ImageGrab.grab(bbox=(50, 1100, 2620, 1400)).save("question.png")  # Fragebereich
    ImageGrab.grab(bbox=(25, 1400, 2620, 1700)).save("answers.png")  # Antwortenbereich


def ocr_with_space(image_path):
    response = requests.post(
        "https://api.ocr.space/parse/image",
        headers={"apikey": os.getenv("SPACE_API_KEY")},
        files={"file": open(image_path, "rb")},
        data={"language": "ger", "isOverlayRequired": False}
    ).json()

    return response.get("ParsedResults", [{}])[0].get("ParsedText", "").strip()


load_dotenv()
client = groq.Client(api_key=os.getenv("GROQ_API_KEY"))

print("Programm läuft... Drücke STRG + ALT + O, um einen Screenshot zu machen.")

while True:
    keyboard.wait("ctrl+alt+o")
    take_screenshots()

    question = ocr_with_space("question.png")
    answers = ocr_with_space("answers.png")

    print(f"\nErkannte Frage: {question}")
    print(f"Erkannte Antworten: {answers}")

    if question and answers:
        response = client.chat.completions.create(
            model="mixtral-8x7b-32768",
            messages=[{"role": "user",
                       "content": f'You are playing Kahoot. The question is: "{question}". The possible answers are: {answers}. Respond with ONLY the correct answer and DON’T explain anything.'}],
            max_tokens=50
        )
        print(f"\nRichtige Antwort: {response.choices[0].message.content.strip()}")
    else:
        print("\nFehler: Frage oder Antworten konnten nicht extrahiert werden.")
