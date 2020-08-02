def wczytaj_plansze(wymiary):

    wiersze = int(wymiary[0])
    kolumny = int(wymiary[1])
    plansza = []

    for x in range(wiersze):
        plansza.append(input("Podaj wiersz: "))

    return plansza