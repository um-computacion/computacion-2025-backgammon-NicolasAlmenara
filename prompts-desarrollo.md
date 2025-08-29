Chat Gpt - version GPT-5 mini
Texto exacto del prompt: "que me recomiendas como board en un programa de backgammon en python, listas o diccionarios?"
Respuesta de la ia: "Te recomiendo usar listas si querés algo simple y rápido, porque el tablero tiene posiciones fijas (0 a 23) y podés acceder por índice.
Usá diccionarios si querés más claridad y facilidad para etiquetar propiedades (color, cantidad, si hay fichas bloqueadas, etc.), aunque sea un poco más pesado."
La salida fue utilizada con cambios, se utilizo una lista de diccionarios.
referencia: core/board.py

Chat gpt - version 4.1
Texto exacto del prompt: "Como hago para que tome un valor aleatorio el dado en un codigo de backgammon en python"
Respuesta de la ia: "import random
dado1 = random.randint(1, 6)
dado2 = random.randint(1, 6)
print(dado1, dado2)"
La salida fue utilizada con cambios, se implemento tambien el caso de dados que dieron el mismo numero.
referencia: core/dice.py


