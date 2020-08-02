def generowanie_planszy(rozmiar_planszy,ilosc_bomb):
    wiersze = int(rozmiar_planszy[0])
    kolumny = int(rozmiar_planszy[1])
    plansza = []
    for x in range(wiersze):
        lista_wierszy = []
        for y in range(kolumny):
            lista_wierszy.append(".")
        plansza.append(lista_wierszy)

    for bomba in range(ilosc_bomb):
        from random import randrange

        bomba_x = int(randrange(wiersze))
        bomba_y = int(randrange(kolumny))

        while plansza[bomba_x][bomba_y] == "*":
            bomba_x = int(randrange(wiersze))
            bomba_y = int(randrange(kolumny))

        plansza[bomba_x][bomba_y] = "*"

    return plansza
