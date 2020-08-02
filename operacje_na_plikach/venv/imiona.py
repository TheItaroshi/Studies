with open("imiona.txt") as imiona:
    lista_imion = []
    for linia in imiona:
        lista_imion.append(linia.strip())
    lista_imion = sorted(lista_imion)
    with open("posotrowane.txt", "w") as posortowane:
        nowy_tekst = ""
        for imie in lista_imion:
            nowy_tekst += imie + "\n"
        posortowane.write(nowy_tekst)
