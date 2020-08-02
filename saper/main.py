from generowanie_planszy import generowanie_planszy
from zliczanie_bomb import zliczanie_bomb


def wczytaj_rozmiar():
    rozmiar_planszy = list()
    rozmiar_planszy.append(input("Podaj liczbę wierszy: "))
    rozmiar_planszy.append(input("Podaj liczbę kolumn: "))
    return rozmiar_planszy


def wczytaj_bomby():
    ilosc_bomb = 0

    while ilosc_bomb == 0:
        ilosc_bomb = input("Podaj ilość bomb: ")
        if ilosc_bomb.isdigit():
            ilosc_bomb = int(ilosc_bomb)
        else:
            print("Podano złe dane!")
            ilosc_bomb = 0

    return ilosc_bomb


def wyswietalnie_planszy(plansza):

    for wiersz in range(len(plansza)):
        print(*plansza[wiersz])


def zakryta_plansza(plansza):
    zakryta = list()
    for wiersz in range(len(plansza)):
        wiersze = []
        for kolumna in range(len(plansza[wiersz])):
            wiersze.append("X")
        zakryta.append(wiersze)

    return zakryta


def integracja(plansza, zakryta, bomby, wymiary):
    wygrana = int(wymiary[0]) * int(wymiary[1]) - bomby
    licznik = 0
    saper = 1
    while saper != "*" and licznik != wygrana:
        licznik += 1
        # if licznik == plansza
        wyswietalnie_planszy(zakryta)

        wspolrzedne = input("Podaj współrzędne(X,Y), które chcesz odkryć: ").split()
        wspolrzedne = [int(x)-1 for x in wspolrzedne]

        saper = plansza[wspolrzedne[1]][wspolrzedne[0]]

        from suma_bomb import suma_bomb
        zakryta[wspolrzedne[1]][wspolrzedne[0]] = suma_bomb(plansza, wspolrzedne[1], wspolrzedne[0])

    if saper == "*":
        print("GAME OVER!")
        from suma_bomb import suma_bomb
        zakryta[wspolrzedne[1]][wspolrzedne[0]] = suma_bomb(plansza, wspolrzedne[1], wspolrzedne[0])
    elif licznik == wygrana:
        print("GRATULACJE WYGRAŁEŚ!")
    return 0


def wyprowadzenie(lista_elementow, l_kolumn):

    l_kolumn = int(l_kolumn)
    liczba_wierszy = len(lista_elementow) / l_kolumn
    poczatek_wiersza = 0

    for v in range(int(liczba_wierszy)):
        koniec_wiersza = (v+1)*l_kolumn
        print(*lista_elementow[poczatek_wiersza:koniec_wiersza])
        poczatek_wiersza = koniec_wiersza

    return 0


wymiary = wczytaj_rozmiar()
bomby = wczytaj_bomby()
dane = generowanie_planszy(wymiary, bomby)
zakryta = zakryta_plansza(dane)
integracja(dane, zakryta, bomby, wymiary)
wynik = zliczanie_bomb(dane)

wyprowadzenie(wynik, wymiary[1])
