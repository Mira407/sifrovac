def zasifruj(text, posun):
    # TODO (A): posuň každé písmeno o 'posun' míst dopředu
    return text


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


zprava = "ahoj svete"
tajne = zasifruj(zprava, 3)
print("Zasifrovano:", tajne)
print("Desifrovano:", desifruj(tajne, 3))