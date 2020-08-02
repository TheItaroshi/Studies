def wprowadzanie_danych():
    try:
        dane_pojazdu = input()
    except EOFError:
        exit()
    return dane_pojazdu

def podzial_danych(dane_pojazdu):
    lista_danych = dane_pojazdu.split()
    if len(lista_danych) != 5:
        return False
    else:
        slownik_danych = {}
        slownik_danych['numer_rejestracyjny'] = lista_danych[0]
        slownik_danych['typ_pojazdu'] = lista_danych[1]
        slownik_danych['metry'] = lista_danych[2]
        slownik_danych['godzina_start'] = lista_danych[3]
        slownik_danych['godzina_koniec'] = lista_danych[4]

        return slownik_danych

def sprawdz_rejestracje(podzielone_dane_pojazdu):
    rejestracja = podzielone_dane_pojazdu['numer_rejestracyjny']
    if rejestracja[0:2].isalpha():
        if rejestracja[2:].isdigit():
            return True
        else:
            return False
    else:
        return False

def sprawdz_typ_pojazdu(podzielone_dane_pojazdu):
    typ_pojazdu = podzielone_dane_pojazdu['typ_pojazdu']
    if typ_pojazdu == "S":
        return "samochod"
    elif typ_pojazdu == "C":
        return "ciezarowka"
    else:
        return False

def sprawdz_czas(podzielone_dane_pojazdu):
    start = podzielone_dane_pojazdu['godzina_start']
    koniec = podzielone_dane_pojazdu['godzina_koniec']

    start = start.split(":")
    koniec = koniec.split(":")

    if start[0].isdigit() and start[1].isdigit() and koniec[0].isdigit() and koniec[1].isdigit():
        start_godziny = int(start[0])
        start_minuty = int(start[1])
        koniec_godziny = int(koniec[0])
        koniec_minuty = int(koniec[1])
    else:
        print("BLAD")
        return "time_error"

    start = int(start_godziny)*60 + int(start_minuty)
    koniec = int(koniec_godziny)*60 + int(koniec_minuty)

    if start_godziny > 24 or start_godziny < 0 or start_minuty > 60 or start_minuty < 0\
            or koniec_godziny > 24 or koniec_godziny < 0 or koniec_minuty > 60 or koniec_minuty < 0:
        print("BLAD")
        return "time_error"

    czas = 1440 - start + koniec

    if czas > 1440:
        czas -= 1440
        return czas
    elif czas < 1440:
        return czas

def sprawdz_predkosc(podzielone_dane_pojazdu,czas):
    odleglosc = podzielone_dane_pojazdu['metry']
    odleglosc = int(odleglosc)/1000
    czas = czas/60

    predkosc = odleglosc/czas
    return predkosc

dane = True

while dane:
    dane = wprowadzanie_danych()
    podzielone_dane = podzial_danych(dane)

    if podzielone_dane == False:
        print("BLAD")
        continue

    if sprawdz_rejestracje(podzielone_dane):
        if sprawdz_typ_pojazdu(podzielone_dane) == "samochod":
            czas = sprawdz_czas(podzielone_dane)

            if czas == "time_error":
                continue

            predkosc = sprawdz_predkosc(podzielone_dane,czas)

            if predkosc > 140:
                print(podzielone_dane['numer_rejestracyjny'],"M","{0:.2f}".format(predkosc))
            else:
                print(podzielone_dane['numer_rejestracyjny'],".","{0:.2f}".format(predkosc))
        elif sprawdz_typ_pojazdu(podzielone_dane) == "ciezarowka":
            czas = sprawdz_czas(podzielone_dane)
            predkosc = sprawdz_predkosc(podzielone_dane,czas)

            if predkosc > 80:
                print(podzielone_dane['numer_rejestracyjny'],"M","{0:.2f}".format(predkosc))
            else:
                print(podzielone_dane['numer_rejestracyjny'],".","{0:.2f}".format(predkosc))
        else:
            print("BLAD")
    else:
        print("BLAD")
