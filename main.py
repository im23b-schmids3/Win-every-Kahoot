import os
import keyboard
import pyautogui
import requests
from openai import OpenAI
from PIL import ImageGrab
from dotenv import load_dotenv


def take_screenshots():
    ImageGrab.grab(bbox=(50, 1200, 2650, 1680)).save("screenshot.png")  # Bereich des Screenshots


def ocr_with_space(image_path):
    response = requests.post(
        "https://api.ocr.space/parse/image",
        headers={"apikey": os.getenv("SPACE_API_KEY")},
        files={"file": open(image_path, "rb")},
        data={"language": "ger", "isOverlayRequired": False}
    ).json()

    return response.get("ParsedResults", [{}])[0].get("ParsedText", "").strip()


load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

print("Programm läuft... Drücke STRG + ALT + O, um einen Screenshot zu machen.")

while True:
    keyboard.wait("ctrl+alt+o")
    take_screenshots()

    screenshot = ocr_with_space("screenshot.png")

    print(f"\nErkannte Texte: {screenshot}")

    if screenshot:
        lines = screenshot.split("\n")

        frage = None
        antwort1 = antwort2 = antwort3 = antwort4 = None
        wahr = falsch = None
        response = None

        if len(lines) >= 5:  # Mindestens eine Frage + 3 Antworten
            frage = lines[0]
            antwort1, antwort2, antwort3, antwort4 = lines[1:5]

            print(f"\nFrage: {frage}")
            print(f"Antwort 1: {antwort1}")
            print(f"Antwort 2: {antwort2}")
            print(f"Antwort 3: {antwort3}")
            print(f"Antwort 4: {antwort4}")

            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user",
                           "content": f'You are playing Kahoot. The question is: "{frage}". The possible answers are: '
                                      f'{antwort1}, {antwort2}, {antwort3}, {antwort4}. If there is no . or " etc. then DONT use it'
                                      f'You are ONLY ALLOWED to Respond with the correct answer and DON’T explain anything. The answers can also be ONLY numbers like 2, 5, 4, 1 for example'}],
                max_tokens=50
            )

        elif len(lines) == 3:  # Eine Frage + 2 Antworten (Wahr/Falsch)
            frage = lines[0]
            wahr = lines[1]
            falsch = lines[2]

            print(f"\nFrage: {frage}")
            print(f"Wahr: {wahr}")
            print(f"Falsch: {falsch}")

            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user",
                           "content": f'You are playing Kahoot. The question is: "{frage}". '
                                      f'The possible answers are: "{wahr}" (True) and "{falsch}" (False). '
                                      f'You are ONLY ALLOWED to Respond with "{wahr}" or "{falsch}" If there is no . or " etc. then DONT use them DON’T explain anything!.'}],
                max_tokens=50
            )

        else:
            print("\nFehler: Nicht genug Zeilen erkannt.")

        if response:
            richtige_antwort = response.choices[0].message.content.strip().lower()
            print(f"\nRichtige Antwort: {richtige_antwort}")

        if antwort1 and richtige_antwort == antwort1.strip().lower():
            pyautogui.moveTo(1100, 1420, duration=0.05)
            pyautogui.click()
        elif antwort2 and richtige_antwort == antwort2.strip().lower():
            pyautogui.moveTo(1100, 1600, duration=0.05)
            pyautogui.click()
        elif antwort3 and richtige_antwort == antwort3.strip().lower():
            pyautogui.moveTo(1900, 1420, duration=0.05)
            pyautogui.click()
        elif antwort4 and richtige_antwort == antwort4.strip().lower():
            pyautogui.moveTo(1900, 1600, duration=0.05)
            pyautogui.click()
        elif wahr and richtige_antwort == wahr.strip().lower():
            pyautogui.moveTo(1250, 1550, duration=0.05)
            pyautogui.click()
        elif falsch and richtige_antwort == falsch.strip().lower():
            pyautogui.moveTo(1900, 1550, duration=0.05)
            pyautogui.click()
        else:
            print("\nFehler: Keine Antwort von der KI erhalten.")

    else:
        print("\nFehler: Frage oder Antworten konnten nicht extrahiert werden.")
