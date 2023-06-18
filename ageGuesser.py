import requests
def nameGuess():
    name = input("What's your name? ")

    answer = requests.get(str('https://api.agify.io/?name=' + name.lower())).json()

    if answer == "none":
        print("I'm sorry, but i can't guess that")
    else:
        print("I'm guessing that you are " + str(answer["age"]) + " years old")

nameGuess()
choice = input("Do you want to try another name? (yes/no) ")

while (choice == "yes"):
    nameGuess()
    choice = input("Do you want to try another name? (yes/no) ")