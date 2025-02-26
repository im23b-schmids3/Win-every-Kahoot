# Gewinne jedes Kahoot Spiel!

Im Moment macht das Skript einen Screenshot von Kahoot, liest den Text mithilfe von Optical Character Recognition (OCR)
aus und gibt ihn aus. Dieser Text wird an Groq AI gesendet, das die Antworten auswertet und die wahrscheinlichste
richtige Antwort zurückgibt. Sobald das Projekt abgeschlossen ist, wird das Skript die richtige Antwort automatisch
selbst auswählen können.

# Wie benutze ich es?

1. Alle nötigen Bibliotheken installieren.
2. Groq API Key beanspruchen und in einem .env File speichern. -> https://groq.com/
3. Space ocr API Key beanspruchen und in einem .env File speichern. -> https://ocr.space/OCRAPI
4. Das Skript ausführen.
5. Einem Kahoot Spiel beitreten und mit ctrl + alt + o einen Screenshot machen.
6. Die Antwort wird in der Konsole ausgegeben.


# Python-Bibliotheken

<ul> 
<li> pip install torch torchvision </li>
<li> pip install requests </li>
<li> pip install keyboard </li>
<li> pip install pillow </li>
<li> pip install pygetwindow </li>
<li> pip install groq </li>
</ul>

# Autor

**[im23b-schmids3](https://github.com/im23b-schmids3)** <br>
Feedback oder Vorschläge? Öffne ein Issue oder erstelle einen Pull-Request!

