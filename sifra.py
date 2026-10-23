POSUN = 3


def zasifruj(text, posun=POSUN):
    vysledek = ""
    for znak in text:
        if "a" <= znak <= "z":
            poradi = ord(znak) - ord("a")
            vysledek += chr((poradi + posun) % 26 + ord("a"))
        else:
            vysledek += znak
    return vysledek

def desifruj(text, posun):
    # TODO (B): posuň každé písmeno o 'posun' míst dozadu
    return text


zprava = "ahoj svee"
tajne = zasifruj(zprava, 3)
print("Zasifrovano:", tajne)
print("Desifrovano:", desifruj(tajne, 3))