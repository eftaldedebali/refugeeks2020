"""
Das Programm so, dass es jede(n) in eurem Team in seiner Heimatsprache begrüßt.
"""


print("Languages: \n1. English\n2. Deutsch\n3. Français\n4. Türkçe ")
language = input( "Please choose your language: ") 

if(language == "1"):
    print("Welcome!")
elif(language == "2"):
    print("Willkommen!")
elif(language == "3"):
    print("Bienvenue!")
elif(language == "4"):
    print("Hoş geldiniz!")
else:
    print("Welcome!")