# Cheat-Sheet



### [Zahlen und Wörter](Datentypen.md)

```python
1, 2, 25, 10000000, 0.1, "hallo", "hallo welt!", """merhzeiliger text
geht so"""
```

### [Listen](Listen.md)

```python
[], [1,2,3,4], range(5), range(5,15,2)
```

### [Rechnen](ErsteSchritte.md)

```python
/ # Division
* # Multiplikation
+ # Addition
- # Subtraktion

5 + 7
4 * 4
```

### [Variablen](Variablen.md)
Variablen können verwendet werden um Zwischenergebnisse zu Speichern, oder einen Wert mehrmals zu verwenden.

```python
a = 50
b = 70
herbert = a + b
```

### [Fallunterscheidung](BedingtesAusfuehren.md)
Mit if können Teile des Programms nur unter bestimmten Bedingungen ausgeführt werden.

```python
if herbert < 121:
    herbert = herbert + 1
```

### [Ein und Ausgabe](ErsteSchritte.md)
```python
print("hallo")
input()
```

### Wiederholung [while](Wiederholungenwhile.md), [for](Wiederholungenfor.md)
```python
while 1 < 2:
    print("go")

for i in range(50):
    print("stop")

for i in "hello":
    print(i)

for i in [25, 25, 1.9, 'hi', 'du']:
    print(i)
```

### [Funktionen](Funktionen.md)
```python
def doFun(name):
   print("hello there", name)

doFun(name="Gollom")
doFun(name="Dobby")
```


