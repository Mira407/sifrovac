def zasifruj(text, posun):
    # TODO (A): posuň každé písmeno o 'posun' míst dopředu
    return text


def desifruj(text, posun):
    vysledek = ""
    for znak in text:
        nova_hodnota = ord(znak) - posun
        # Pokud jsme se dostali před 'a', skočíme na konec abecedy
        if nova_hodnota < ord('a'):
            nova_hodnota += 26
        
        vysledek += chr(nova_hodnota)
    return vysledek


zprava = "ahoj svete"
tajne = zasifruj(zprava, 3)
print("Zasifrovano:", tajne)
print("Desifrovano:", desifruj(tajne, 3))