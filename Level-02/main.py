from os import name


print("============================\n " "Dein Persönliches Haustier\n============================")

def question():
    print("Was möchtest du tun?\n \n1. füttern\n2. streicheln\n3. spielen\n4. schlafen\n5. Beenden")

def main():
    print ("Wie möchtest du dein Haustier nennen?\n>> ",end= "")
    name = input()
    if name:
        print(f"Hallo! Ich bin {name}!\nSchön dich kennenzulernen!")
    else:
        print(f"Hallo! Ich bin Artemis!\nSchön dich kennenzulernen!")
    question()

def feed(): 
    input_value = input("Möchtest du dein Haustier füttern? (ja/nein)\n>")
    if input_value == "ja":
        print(f"Du hast {name} gefüttert!\n " f"{name} ist jetzt satt!")
        question()

    elif input_value == "nein":
        question()

def stroke():
    input_value = input("Möchtest du dein Haustier streicheln? (ja/nein)\n>")
    if input_value == "ja":
        print(f"Du hast {name} gestreichelt!\n " f"{name} ist jetzt glücklich!")
        question()

    elif input_value == "nein":
        question()

def play():
    input_value = input("Möchtest du mit deinem Haustier spielen? (ja/nein)\n>")
    if input_value == "ja":
        print(f"Du hast mit {name} gespielt!\n " f"{name} ist jetzt müde!\n")
        sleep()

    elif input_value == "nein":
        question()

def sleep():
    input_value = input("Möchtest du dein Haustier schlafen lassen? (ja/nein)\n>")
    if input_value == "ja":
        print(f"{name} schläft jetzt!\n " f"{name} ist jetzt ausgeruht!")
        question()

    elif input_value == "nein":
        question()

def exit():
    print("Auf Wiedersehen!")
    quit()

def quit():
    print("Auf Wiedersehen!")
    exit()

def list():
    list = {1: "füttern", 2: "streicheln", 3: "spielen", 4: "schlafen", 5: "Beenden"}

def difinition():
    if 1 in list:
        feed()
    elif 2 in list:
        stroke()
    elif 3 in list:
        play()
    elif 4 in list:
        sleep()
    elif 5 in list:
        print("Auf Wiedersehen!")
        exit()

main()
feed()
stroke()
play()
sleep()
exit()

