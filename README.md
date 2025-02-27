# Gewinne jedes Kahoot Spiel!

Das Skript erstellt per Tastenkombination (Ctrl + Alt + O) einen Screenshot, extrahiert den Text mithilfe von Optical
Character Recognition (OCR) und gibt ihn aus. Anschliessend wird dieser Text an ChatGPT gesendet, das mögliche Antworten
analysiert und die wahrscheinlich beste Lösung zurückgibt. Diese wird dann automatisch mit pyautogui angeklickt.

# Wie benutze ich es?

1. Alle nötigen Bibliotheken installieren.
2. OpenAI API Key beanspruchen und in einem .env File speichern. -> https://openai.com/index/openai-api/
3. Space ocr API Key beanspruchen und in einem .env File speichern. -> https://ocr.space/OCRAPI
4. Das Skript ausführen.
5. Einem Kahoot Spiel beitreten und mit ctrl + alt + o einen Screenshot machen.
6. Die Antwort wird automatisch für Sie angeklickt.

# Python-Bibliotheken

<ul> 
<li> pip install torch torchvision </li>
<li> pip install requests </li>
<li> pip install keyboard </li>
<li> pip install pyautogui </li>
<li> pip install pillow </li>
<li> pip install pygetwindow </li>
<li> pip install openai </li>
</ul>

# Hinweis

Das Skript kann keine Bilder ohne Text erkennen oder Puzzle-Fragen lösen.

# Autor

**[im23b-schmids3](https://github.com/im23b-schmids3)** <br>
Feedback oder Vorschläge? Öffne ein Issue oder erstelle einen Pull-Request!

