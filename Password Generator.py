import random
import os 
from time import sleep

clear = lambda: os.system('cls')

CHOISES = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '@', '#', '$', '%', '^', '&', '*']

def generator():
    generated_password = []

    while True:
        amount_of_letters = input("How many letters would you like to be in the password? ")
        amount_of_passwords = input("How many passwords would you like to be generated? ")

        try:
            amount_of_letters = int(amount_of_letters)
            amount_of_passwords = int(amount_of_passwords)
            clear()
            break
        except ValueError:
            print("Please enter a number.")
            sleep(2)
            clear()
            continue

    print("Generating Passwords...")

    sleep(3)
    clear()

    print("Here are your passwords: \n")

    for _ in range(amount_of_passwords):
        for _ in range(amount_of_letters):
            choise = random.choice(CHOISES)
            generated_password.append(choise)
        print("".join(generated_password)) # join makes it have none of the list elemnts and replace them with an blank space
        generated_password.clear()

    input("\nPress enter to exit")

generator()