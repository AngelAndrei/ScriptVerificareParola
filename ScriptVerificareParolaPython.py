import time
import re

def password_strength_checker(password):
    if len(password) < 8:
        return "Parola slabă: Parola trebuie să aibă măcar 8 caractere"
    # verificare minuscule
    if not re.search("[a-z]", password):
        return "Parola slabă: Parola trebuie să conțină măcar un caracter minuscul."
    # verificare majuscule
    if not re.search("[A-Z]", password):
        return "Parola slabă: Parola trebuie să conțină măcar un caracter majuscul."
    # verificare numere
    if not re.search("[0-9]", password):
        return "Parola slabă: Parola trebuie să conțină măcar un număr."
    # verificare caractere speciale
    if not re.search("[!@#$%^&*()_+=-:;><.,/]", password):
        return "Parola slabă: Parola trebuie să conțină măcar un caracter special."

    return "Parola puternică"

def main():
    password = input("Introdu parola:  ")

    for _ in range(3):
        print(".", end="")
        time.sleep(1)
    print("\nGata")

    result = password_strength_checker(password)
    print(result)

if __name__ == "__main__":
    main()
