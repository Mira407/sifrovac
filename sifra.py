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
    vysledek = ""
    for znak in text:
        # Zpracujeme pouze malá písmena (a-z)
        if 'a' <= znak <= 'z':
            nova_hodnota = ord(znak) - posun
            if nova_hodnota < ord('a'):
                nova_hodnota += 26
            vysledek += chr(nova_hodnota)
        else:
            # Ostatní znaky necháme beze změny
            vysledek += znak
    return vysledek


zprava = "ahoj svee"
tajne = zasifruj(zprava, 3)
print("Zasifrovano:", tajne)
print("Desifrovano:", desifruj(tajne, 3))