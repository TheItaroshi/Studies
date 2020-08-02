def pobierz_element(plansza, a, b):

    liczba_wierszy = len(plansza)

    for x in range(liczba_wierszy):
        liczba_kolumn = len(plansza[x])
        if a < 0 or b < 0:
            return ""

        if a >= liczba_wierszy:
            return ""

        if b >= liczba_kolumn:
            return ""

    return plansza[a][b]

plansza = ["**...", ".....", ".*..."]

assert pobierz_element(plansza, -1, 0) == ""
assert pobierz_element(plansza, 0, -1) == ""
assert pobierz_element(plansza, 3, 0) == ""
assert pobierz_element(plansza, 0, 5) == ""
assert pobierz_element(plansza, 0, 1) == "*"
assert pobierz_element(plansza, 2, 0) == "."
