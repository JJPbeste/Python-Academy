pet_name = "Artemis"

print("============================\nDein Persönliches Haustier\n============================")


def question():
    print("Was möchtest du tun?\n\n1. füttern\n2. streicheln\n3. spielen\n4. schlafen\n5. Beenden")


def main():
    global pet_name
    print("Wie möchtest du dein Haustier nennen?\n>> ", end="")
    user_name = input()
    if user_name:
        pet_name = user_name
        print(f"Hallo! Ich bin {pet_name}!\nSchön dich kennenzulernen!")
    else:
        pet_name = "Artemis"
        print(f"Hallo! Ich bin {pet_name}!\nSchön dich kennenzulernen!")
    question()
    definition()


def feed():
    input_value = input("Möchtest du dein Haustier füttern? (ja/nein)\n>")
    if input_value == "ja":
        print(f"Du hast {pet_name} gefüttert!\n{pet_name} ist jetzt satt!")
        question()
        definition()
    elif input_value == "nein":
        question()
        definition()


def stroke():
    input_value = input("Möchtest du dein Haustier streicheln? (ja/nein)\n>")
    if input_value == "ja":
        print(f"Du hast {pet_name} gestreichelt!\n{pet_name} ist jetzt glücklich!")
        question()
        definition()
    elif input_value == "nein":
        question()
        definition()


def play():
    input_value = input("Möchtest du mit deinem Haustier spielen? (ja/nein)\n>")
    if input_value == "ja":
        print(f"Du hast mit {pet_name} gespielt!\n{pet_name} ist jetzt müde!\n")
        sleep()
    elif input_value == "nein":
        question()
        definition()


def sleep():
    input_value = input("Möchtest du dein Haustier schlafen lassen? (ja/nein)\n>")
    if input_value == "ja":
        print(f"{pet_name} schläft jetzt!\n{pet_name} ist jetzt ausgeruht!")
        question()
        definition()
    elif input_value == "nein":
        question()
        definition()

def status():
    pass    

def status():
    create_status = input("Möchtest du den Status deines Haustiers sehen? (ja/nein)\n>")
    if create_status == "ja":
        status = {
        "Name": pet_name,
        "Hunger": "Satt",
        "Glück": "Glücklich",
        "Energie": "Ausgeruht"
         }
        print("Status deines Haustiers:")
        
    else:
        question()
        definition()
        pass


def quit_program():
    print("Auf Wiedersehen!")
    raise SystemExit


def definition():
    choice = input("Wähle eine Option (1-5): ")
    if choice == "1":
        feed()
    elif choice == "2":
        stroke()
    elif choice == "3":
        play()
    elif choice == "4":
        sleep()
    elif choice == "5":
        quit_program()
    else:
        print("Ungültige Auswahl.")
        question()
        definition()


main()
