def zasifruj(text, posun):
    # TODO (A): posuň každé písmeno o 'posun' míst dopředu
    return text


def desifruj(text, posun):
    vysledek = ""
    for znak in text:
        # Převedeme znak na číslo, odečteme posun a vrátíme zpět na znak
        vysledek += chr(ord(znak) - posun)
    return vysledek


zprava = "ahoj svete"
tajne = zasifruj(zprava, 3)
print("Zasifrovano:", tajne)
print("Desifrovano:", desifruj(tajne, 3))