def wprowadzenie_liczb():

    ilosc_liczb = input("Podaj ilość liczb, które chcesz sprawdzić: ")
    if ilosc_liczb.isdigit() and int(ilosc_liczb) != 0:
        ilosc_liczb = int(ilosc_liczb)
        liczby = []

        for x in range(ilosc_liczb):
            liczba_wejscie = input("Podaj liczbę nr." + str(x+1) + " ")

            if liczba_wejscie.isdigit():
                liczba = int(liczba_wejscie)
                liczby.append(liczba)
            else:
                liczby.append(-1)
        return liczby
    else:
        return [-1]


def liczby_tribonacciego():

    tablica_tribocnacciego = [0, 1, 2]

    nastepna_liczba = (tablica_tribocnacciego[-1] + tablica_tribocnacciego[-2] + tablica_tribocnacciego[-3])

    while nastepna_liczba <= 1000000000000:
        tablica_tribocnacciego.append(nastepna_liczba)
        nastepna_liczba = (tablica_tribocnacciego[-1] + tablica_tribocnacciego[-2] + tablica_tribocnacciego[-3])

    return tablica_tribocnacciego


def sprawdzanie_liczb(tablica_liczb):

    for liczba in tablica_liczb:
        if liczba < 0 or liczba > 1000000000000:
            print("BLAD")
        else:
            if liczba in liczby_tribonacciego():
                print(str(liczba) + "\tTAK - liczba należy do ciągu Tribonnaciego")
            else:
                print(str(liczba) + "\tNIE - liczba nie należy do ciągu Tribonnaciego")

    return tablica_liczb


dane = wprowadzenie_liczb()
sprawdzone_dane = sprawdzanie_liczb(dane)
