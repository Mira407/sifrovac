POSUN = 3

def zasifruj(text, posun=POSUN):
    vysledek = ""
    for znak in text:
        vysledek += chr(ord(znak) + posun)
    return vysledek



def desifruj(text, posun):
    # TODO (B): posuň každé písmeno o 'posun' míst dozadu
    return text


zprava = "ahoj svete"
tajne = zasifruj(zprava, 3)
print("Zasifrovano:", tajne)
print("Desifrovano:", desifruj(tajne, 3))