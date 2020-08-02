from abc import ABC, abstractmethod
import pickle

class Konto:                                #utworzenie klasy Konto
    def __init__(self, stan_konta=0):       #utworzenie konstruktora klasy z argumentem postawowym stan_konta = 0
        self._stan_konta = stan_konta

    def get_stan_konta(self):               #utowrzenie metody get_stan_konta zwracającej wartość pola stan_konta
        return self._stan_konta

    def wplata(self, kwota):                #utworzenie metody wplata zwiększającej wartosc pola stan_konta
        self._stan_konta += kwota

    def wyplata(self, kwota):               #utworzenie metody wyplata zmniejszającej wartośc pola stan_konta
        try:
            if (self._stan_konta - kwota) < 0:  #warunek wywołania metody
                raise WyplataException()        #wywołanie wyjątku WyplataException
            else:
                self._stan_konta -= kwota
        except WyplataException as bladWyplaty:
            bladWyplaty.get_komunikat()         #wywołanie metody get_komuniakt wyjątku WyplataException


class KontoBankowe(Konto):                      #utworzenie klasy KontoBankowe dziedziczącej po klasie Konto
    def __init__(self, nazwisko, stan_konta):   #utworzenie konstruktora klasy
        super().__init__(stan_konta)            #dziedziczenie kontruktora klasy dla pola stan_konta
        self._nazwisko = nazwisko

    def get_nazwisko(self):                 #utworzenie metody get_nazwisko zwracającej wartość pola nazwisko
        return self._nazwisko


class KontoOsobiste(KontoBankowe):              #utworzenie klasy KontoOsobiste dziedziczącej po klasie KontoBankowe
    def __init__(self, minimalny_stan_konta, nazwisko, stan_konta):
        super().__init__(nazwisko, stan_konta)
        self._minimalny_stan_konta = minimalny_stan_konta

    def get_minimalny_stan_konta(self):         #utworzenie metody get_minimalny_stan_konta zwracającej wartość pola minimalny_stan_konta
        return self._minimalny_stan_konta

    def wyplata(self, kwota):                   #przeciążenie metody wypłata
        try:
            if (self._stan_konta-kwota) < self._minimalny_stan_konta:   #zmiana warunku wywołania metody
                raise WyplataException()        #wywołanie wyjątku WyplataException
            else:
                self._stan_konta -= kwota
        except WyplataException as bladWyplaty:
            bladWyplaty.get_komunikat()         #wywołanie metody get_komuniakt wyjątku WyplataException


class RaportKonta:                              #utowrzenie klasy RaportKonta

    @staticmethod                               #dekorator metody statycznej
    def raport(konto):                          #utowrzenie metody statycznej pobierającej informacje o obiektach klasy Konto
        if isinstance(konto, KontoOsobiste):
            print("Stan konta:", str(konto.get_stan_konta()), "zł")
            print("Nazwisko właściciela: ", konto.get_nazwisko())
            print("Minimalny stan konta: ", konto.get_minimalny_stan_konta())
        elif isinstance(konto, KontoBankowe):
            print("Stan konta:", str(konto.get_stan_konta()), "zł")
            print("Nazwisko właściciela: ", konto.get_nazwisko())
        elif isinstance(konto, Konto):
            print("Stan konta:", str(konto.get_stan_konta()), "zł")


class KontoException(Exception):                #utworzenie wyjątku KontoException dziedziczącego po klasie Exception
    def __init__(self):
        super().__init__()                      #dziedziczenie konstruktora
        self.komunikat = ""

    def get_komunikat(self):                    #utworzenie metody get_komunikat zwracającej wartośc pola komunikat
        print(self.komunikat)


class WyplataException(KontoException):         #utworzenie wyjątku WyplataException dziedziczącego po klasie KontoException
    def __init__(self):
        super().__init__()                      #dziedziczenie konstruktora
        self.komunikat = "Brak wystarczających środków do wypłaty."


class NieudanyPrzelewException(KontoException): #utworzenie wyjątku NieudanyPrzelewException dziedziczącego po klasie KontoException
    def __init__(self):
        super().__init__()                      #dziedziczenie konstruktora
        self.komunikat = "Nie udało się wykonać przelewu, brak wystarczających środków na koncie."


class NumerKontaException(KontoException):      #utworzenie wyjątku NumerKontaException dziedziczącego po klasie KontoException
    def __init__(self):
        super().__init__()                      #dziedziczenie konstruktora
        self.komunikat = "Nie udało się wykonać przelewu, brak konta o podanym numerze."


class Bank:                                     #utworzenie klasy Bank
    def __init__(self, nazwa_banku="mBank"):
        self._nazwa_banku = nazwa_banku
        self._lista_kont = list()               #utworzenie pola lisa_konta będącego listą obiektów

    def przelew(self, nr_konta_nadawcy, nr_konta_odbiorcy, kwota_przelewu):     #utworzenie metody przelew zmieniającej wartości pól stan_konta obiektów z listy lista_kont
        try:
            if nr_konta_nadawcy >= len(self._lista_kont) or nr_konta_odbiorcy >= len(self._lista_kont):
                raise NumerKontaException()     #wywołanie wyjątku NumerKontaException
            else:
                try:
                    if self._lista_kont[nr_konta_nadawcy].get_stan_konta() < kwota_przelewu:
                        raise NieudanyPrzelewException()    #wywołanie wyjątku NieudanyPrzelewException
                    else:
                        self._lista_kont[nr_konta_nadawcy]._stan_konta -= kwota_przelewu
                        self._lista_kont[nr_konta_odbiorcy]._stan_konta += kwota_przelewu
                except NieudanyPrzelewException as nieudanyPrzelew:
                    nieudanyPrzelew.get_komunikat()         #wywołanie metody get_komunikat wyjątku NieudanyPrzelewException
        except NumerKontaException as numerKonta:
            numerKonta.get_komunikat()                      #wywołanie metody get_komuniakt wyjątku NumerKontaExcpetion

    def dodaj_konto(self, konto):               #utworzenie metody dodaj_konto dodającej obiekty do listy lista_kont
        self._lista_kont.append(konto)

    def usun_konto(self, nr_konta):             #utworzenie metody usun_konto usuwającej obiekt o podanym indeksie z listy lista_kont
        del self._lista_kont[nr_konta]

    def raport_konta_osobiste(self):            #utworzenie metody raport_konta_osobiste wyświetlającą informacje na temat obiektów klasy KontoOsobiste
        suma_kont = 0
        suma_srodkow_na_kontach = 0
        for konto in self._lista_kont:
            if isinstance(konto, KontoOsobiste):    #sprawdzenie czy dany obiekt jest instacją klasy KontoOsobiste
                suma_kont += 1
                suma_srodkow_na_kontach += konto.get_stan_konta()
        print("Suma kont osobistych w naszym bank:", suma_kont, "\nSuma środków zgromadzonych na kontach:",
              suma_srodkow_na_kontach)

    def raport_wszystkie(self):                 #utworzenie metody raport_konta_osobiste wyświetlającą informacje na temat obiektów klasy Konto
        suma_kont = 0
        suma_srodkow_na_kontach = 0
        for konto in self._lista_kont:
            if isinstance(konto, Konto):            #sprawdzenie czy dany obiekt jest instacją klasy Konto
                suma_kont += 1
                suma_srodkow_na_kontach += konto.get_stan_konta()
        print("Suma kont w naszym bank:", suma_kont, "\nSuma środków zgromadzonych na kontach:",
              suma_srodkow_na_kontach)

class IteratorBanku:                                                    #utworzenie klasy IteratorBanku
    def __init__(self, bank):                                           #utworzenie konstruktora pobierającego argument klasy Bank
        self.lista_kont = bank._lista_kont                              #pobranie listy kont z obiektu klasy Bank
        self.koniec_iteracji = len(bank._lista_kont)                    #określenie końca iteracji na podstawie długości listy lista_kont obiektu klasy Bank
        self.iteracja = 0                                               #określenie początku iteracji (int = 0)

    def __iter__(self):                                                 #utworzenie metody iter inicjującej iterację
        return self                                                     #zwrócenie obiektu naszego iteratora (samego siebie)

    def __next__(self):                                                 #utworzenie metody next zwracajacej wartość danego elementu
                                                                                # oraz przechącej do następnego (jeśli istnieje)
        if self.iteracja >= self.koniec_iteracji:                       #warunek kończący iterację
            raise StopIteration                                         #wywołanie wyjątku StopIteration kończącego iterację
        if isinstance(self.lista_kont[self.iteracja],KontoBankowe):     #warunek określający typ iterowanego elementu (czy jest to obiekt klasy KontoBankowe)
            komunikat = "Konto nr " + str(self.iteracja+1) + " - " \
                        + str(self.lista_kont[self.iteracja].get_stan_konta()) \
                        + "zł, właścicielem konta jest: " \
                        + str(self.lista_kont[self.iteracja].get_nazwisko()) #przypisane wartości zmiennej komuniakt dla elementu klasy KontoBankowe

        else:
            komunikat = "Konto nr "+ str(self.iteracja+1) + " - " \
                        + str(self.lista_kont[self.iteracja].get_stan_konta()) \
                        + "zł, brak informacji o właścicielu konta"         #przypisane wartości zmiennej komuniakt dla elementu klasy Konto
        self.iteracja += 1                                                  #zwiększenie pola iteracja o (int = 1) (przejśce do kolejnego elementu iteracji)
        return komunikat                                                    #zwrócenie wartości zmiennej komunikat (wyświetlenie inforacji o elemencie iteracji)

class ZapisException(Exception):            #utworzenie wyjątku ZapisException dziedziczącego po klasie Exception
    def __init__(self):
        super().__init__()                  #dziedziczenie konstrutora klasy
        self.komunikat = "Wystąpił błąd przy próbie zapisania pliku, upewnij się, że obiekt, który chcesz zapisać jest" \
                         "obiektem właściwej klasy!"

    def get_komunikat(self):                #utworzenie metody get_komunikat zwracającej wartość pola komunikat
        print(self.komunikat)

class Zapis(ABC):                           #utworzenie klasy abstrakcyjnej Zapis dziedziczącej po klasie ABC
    @abstractmethod                         #dekorator metody abstrakcyjnej
    def zapisz_na_dysk(slef, obiekt):
        pass


class Odczyt(ABC):                          #utworzenie klasy abstrakcyjnej Odczyt dziedziczącej po klasie ABC
    @abstractmethod                         #dekorator metody abstrakcyjnej
    def odczytaj_z_dysku(self):
        pass


class ZapisBank(Zapis):                     #utworzenie klasy ZapisBank dziedziczącej po klasie Zapis
    def __init__(self, nazwa_pliku = "plik_banku", typ_zapisu = "wb"): #utworzenie konstruktora z parametrami domyślnymi
        self.nazwa_pliku = nazwa_pliku + ".txt"
        self.typ_zapisu = typ_zapisu

    def zapisz_na_dysk(self, obiekt):       #przeciążenie metody abstrakcyjnej zapisz_na_dysk zapisującej dany obiekt do pliku
        if isinstance(obiekt,Bank):     #sprawdzenie czy dany obiekt jest instancją klasy bank
            with open(self.nazwa_pliku, self.typ_zapisu) as plik:  # przypisanie wartości funkcji open() do słowa kluczowego plik
                pickle.dump(obiekt, plik)                          # zapisanie zserializowanego obiektu do pliku
            print("Zapisano obiekt do pliku: " + self.nazwa_pliku)
        else:
            raise ZapisException  # wywołanie wyjątku ZapisException


class OdczytajBank(Odczyt):                 #utworzenie klasy OdczytajBank dziedziczącej po klasie Odczyt
    def __init__(self, nazwa_pliku = "plik_banku", typ_odczytu = "rb"): #utworzenie konstruktora z parametrami domyślnymi
        self.nazwa_pliku = nazwa_pliku + ".txt"
        self.typ_odczytu = typ_odczytu

    def odczytaj_z_dysku(self):             #przeciążenie metody abstrakcyjnej odczytaj_z_dysku odczytującej obiekt z pliku
        with open(self.nazwa_pliku, self.typ_odczytu) as plik:  #przypisanie wartości funkcji open() do słowa kluczowego plik
            return pickle.load(plik)        #zwrócenie zdeserializowanej wartości obiektu z pliku
