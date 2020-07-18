# Schrittweises Zeichnen des Galgenmännchens

Zunächst müssen die einzelnen Schritte des Galgenmännchens einzeln von jeweils einer Funktion gezeichnet werden. Erstellen Sie hierfür ein eigenes Modul `hangmanschritte`. Wenn sie sich jetzt fragen woher sie denn wissen sollen wie das geht? Das heißt so viel wie erstellen Sie eine neue Datei mit dem Namen `hangmanschritte.py` und lösen Sie darin die hier gestellten Aufgaben.

### Eine Funktion für den Hügel

Als Beispiel wird zunächst der Hügel gezeichnet.

```python

def huegel():
  t.left(90)
  t.penup()
  t.backward(200)
  t.pendown()
  t.circle(100,180)
  t.right(90)
  t.penup()
  t.backward(100)
  t.right(90)
  t.forward(100)
  t.pendown()
```

### Jeder Schritt brauch eine Funktion

Nachdem nun der Hügel gezeichnet werden kann muss für jeden Der Schritte eine Funktion geschrieben werden. Es ist sinnvoll, am Ende jeder Funktion zu dem Punkt zu fahren, wo die nächste Funktion weiter machen muss.

Die zu schreibenden Funktionen sind:

  * `huegel`
  * `senkrechte`
  * `waagerechte`
  * `stütze` (kleiner diagonaler Stützbalken zwischen senkrechter und waagerechter)
  * `seil`
  * `kopf` (mit Gesicht)
  * `körper`
  * `arme`
  * `beine`

Um das schon erstellte zu testen müssen die Funktionen jeweils aufgerufen werden. Die Zeilen außer Hügel sind noch mit einer `#` auskommentiert (also deaktiviert). Sobald die entsprechende Funktion geschrieben ist kann das `#` entfernt werden:

```python
if __name__ == "__main__":
    huegel()
    #senkrechte()
    #waagerechte()
    #stütze()
    #seil()
    #kopf()
    #körper()
    #arme()
    #beine()
```

> ### Notiz
> Die findigen werden ein seltsames `if` bemerkt haben. Diese bedeutet, dass der Programmcode nur dann ausgeführt wird, wenn das Modul direkt gestartet wird, nicht aber, wenn es in ein anderes Modul eingebunden wird.

### Noch eine Hilfe für den `steps`-Schritt

Diese Funktion ist viel einfacher:

```python
def senkrechte():
    t.forward(300)
    t.right(90)
```

Die Funktionen müssen alle vor den Aufrufen sein. Das heißt am einfachsten ist, man importiert turtle usw. dann definiert man die Funktionen und erst danach kommen die Aufrufe. Wurde auch die Senkrechte Funktion definiert kann das `#` vor `senkrechte()` entfernt werden.

Es sollte jetzt kein Problem mehr sein alle nötigen Funktionen zu Definieren.

Wenn alles gezeichnet ist sollte das Ganze so aussehen:

![Hangman Schritte](img/hangmansteps.png)

Natürlich darf diese Grafik nach belieben angepasst werden, sodass jeder etwas anderes aufhängt... oder es kann die gewaltfreie Version gemacht werden, indem man eine Blume schrittweise zeichnet.