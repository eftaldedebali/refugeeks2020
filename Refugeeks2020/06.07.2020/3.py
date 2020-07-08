"""
Das Prpgram so, dass es nur Aline und Fabian mit ihren Namen begrüßt und alle anderen mit "Hallo Freund"
"""

name = input("Was heißen Sie?: ")
if name.lower() != ("fabian") and name.lower() != ("aline"):
   name = "Freund"
print ("Hallo " + name)