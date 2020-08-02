def zliczanie_bomb(plansza):
    from suma_bomb import suma_bomb

    wynikowa = []
    liczba_wierszy = len(plansza)
    for a in range(liczba_wierszy):
        liczba_kolumn = len(plansza[a])
        for b in range(liczba_kolumn):
            if plansza[a][b] == "*":
                wynikowa.append("*")
            else:
                suma_bomb(plansza, a, b)
                wynikowa.append(suma_bomb(plansza, a, b))
    return wynikowa