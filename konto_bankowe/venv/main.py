# projekt Konto_bankowe, w dalszej części komentarzy referencje do obketów są nazywane obiektami:

from konto import *                             #zaimportowanie klas i modułów z pliku konto.py

konto1 = Konto(1000)                            #utworzenie obiektu klasy Konto -> stan_konta = 1000
konto2 = KontoBankowe("Janas", 2000)            #utworzenie obiektu klasy KontoBankowe -> nazwisko = "Janas", stan_konta = 2000
konto3 = KontoOsobiste(0, "Kowalski", 3000)     #utworzenie obiektu klasy KontoOsobiste -> minimalny_stan_konta = 0, nazwisko = "Kowalski", stan_konta = 3000
konto4 = KontoOsobiste(0, "Ratajczak", 3000)    #utworzenie obiektu klasy KontoOsobiste -> minimalny_stan_konta = 0, nazwisko = "Ratajczak", stan_konta = 3000
konto5 = KontoOsobiste(0, "Borowski", 3000)     #utworzenie obiektu klasy KontoOsobiste -> minimalny_stan_konta = 0, nazwisko = "Borowski", stan_konta = 3000
konto6 = KontoOsobiste(0, "Kosmyk", 3000)       #utworzenie obiektu klasy KontoOsobiste -> minimalny_stan_konta = 0, nazwisko = "Kosmyk", stan_konta = 3000

bank = Bank()                                   #utworzenie obiektu klasy Bank

bank.dodaj_konto(konto1)                        #
bank.dodaj_konto(konto2)                        #
bank.dodaj_konto(konto3)                        #Przypisanie obiektów klasy Konto do listy obiektów w klasie Bank
bank.dodaj_konto(konto4)                        #
bank.dodaj_konto(konto5)                        #
bank.dodaj_konto(konto6)                        #

raport = RaportKonta()                          #utowrzenie obiektu klasy RaportKonta

print("Raport konto1:")
raport.raport(konto1)                           #Wywołanie metody raport(), obiektu raport dla zmiennej konto1 będącej obiektem klasy Konto
print("\nRaport konto2:")
raport.raport(konto2)                           #Wywołanie metody raport(), obiektu raport dla zmiennej konto2 będącej obiektem klasy KontoBankowe
print("\nRaport konto3:")
raport.raport(konto3)                           #Wywołanie metody raport(), obiektu raport dla zmiennej konto3 będącej obiektem klasy KontoOsobiste


konto3.wplata(100)                              #Wywołanie metody wplata(), obiektu konto3 dla zmiennej (int = 100) -> stan_konta += 100
print("\nRaport konto3 po wpłacie 100zł:")
raport.raport(konto3)                           #Wywołanie metody raport(), obiektu raport dla zmiennej konto3 będącej obiektem klasy KontoOsobiste
print("\nRaport konto3 po wypłacie 50zł :")
konto3.wyplata(50)                              #Wywołanie metody wplata(), obiektu konto3 dla zmiennej (int = 100) -> stan_konta -= 50
raport.raport(konto3)                           #Wywołanie metody raport(), obiektu raport dla zmiennej konto3 będącej obiektem klasy KontoOsobiste

# Projekt wyjatki:

print("-----------------\nWYJĄTKI\n-----------------")
print("{}zł - stan konta nr1 przed przelewem".format(konto1.get_stan_konta()))      #wywołanie metody format() funkcji str oraz metody get_stan_konta klasy Konto
print("{}zł - stan konta nr3 przed przelewem\n".format(konto3.get_stan_konta()))    #wywołanie metody format() funkcji str oraz metody get_stan_konta klasy Konto

bank.przelew(0,2,1000)              #wywolanie metody przelew klasy Bank dla indeksów 0 i 2 z listy_kont obiektu bank o wartości (int = 1000)
                                            # -> stan_konta (obiekt z listy o indeksie 0) -= 1000, stan_konta (obiekt z listy o indeksie 2) += 1000

print("{}zł - stan konta nr1 po przelewie".format(konto1.get_stan_konta()))         #wywołanie metody format() funkcji str oraz metody get_stan_konta klasy Konto
print("{}zł - stan konta nr3 po przelewie\n".format(konto3.get_stan_konta()))       #wywołanie metody format() funkcji str oraz metody get_stan_konta klasy Konto

bank.przelew(0,2,1000)              #wywolanie metody przelew klasy Bank dla indeksów 0 i 2 z listy_kont obiektu bank o wartości (int = 1000)
                                            # -> wywołanie wyjątku NieudanyPrzelewException i metody jego klasy get_komunikat()

# Projekt obiekty w strukturach danych:

print("-----------------\nOBIEKTY W STRUKTURACH DANYCH\n-----------------")

bank.przelew(2,5,1000)              #wywołanie metody przelew klasy Bank dla indeksów 2 i 5 z listy_kont obiektu bank o wartości (int = 1000)
                                            # -> stan_konta (obiekt z listy o indeksie 2) -= 1000, stan_konta (obiekt z listy o indeksie 5) += 1000
bank.usun_konto(5)                  #wywołanie metody usun_konto klasy Bank dla u 5 z listy_kont obiektu bank
                                            # -> lista_kont obiektu bank zawiera 5 elementów [konto1,konto2,konto3,konto4,konto5]
bank.przelew(2,5,1000)              #wywołanie metody przelew klasy Bank dla indeksów 2 i 5 z listy_kont obiektu bank o wartości (int = 1000)
                                            # -> wywołanie wyjątku NumerKontaException i metody jego klasy get_komunikat()
print("\n")
bank.raport_konta_osobiste()        #wywołanie metody raport_konta_osobite klasy Bank obiektu bank
                                            # -> wypisanie sumy obiektów klasy KontoOsobite oraz sumy wartości pól stan_konta tych obiektów,
                                                    #będących elementami listy lista_kont obiektu bank
print("\n")
bank.raport_wszystkie()             #wywołanie metody raport_wszystkie klasy Bank obiektu bank
                                            # -> wypisanie sumy obiektów klasy Konto oraz sumy wartości pól stan_konta tych obiektów,
                                                    #będących elementami listy lista_kont obiektu bank

print("-----------------\nITERATORY\n-----------------")


iterator = IteratorBanku(bank)      #utworzenie iteratora klasy IteratorBanku dla obiektu bank -> pobranie listy kont obiektu bank
for x in iterator:                  #wykonanie pętli for dla obiektu iterator -> wypisanie wartości kolejnych pól z listy lista_kont iteratora
    print(x)

print("-----------------\nZAPIS OBIEKTÓW\n-----------------")

zapis_banku = ZapisBank()       #utowrzenie obiektu zapis_banku klasy ZapisBank
odczyt_banku = OdczytajBank()   #utworzenie obiektu odczyt_banku klasy OdczytajBank
try:
    zapis_banku.zapisz_na_dysk(bank)  # wywołanie metody zapisz_na dysk obiektu zapis_banku dla argumentu bank
                                            # -> zapisanie obiektu bank do pliku
    zapis_banku.zapisz_na_dysk(konto1)  # wywołanie metody zapisz_na dysk obiektu zapis_banku dla argumentu konto1
                                            # -> wywołanie wyjątku ZapisException
except ZapisException as zapis:
    zapis.get_komunikat()  # wywołanie metody get_komuniakt wyjatku ZapisExpcetion

del bank                            #usunięcie obiektu bank

try:
    bank.raport_wszystkie()         #próba wywolania metody obiektu bank -> wywołanie błedu (obiekt nie istnieje)
except NameError:
    print("\nBrak obiektu o podanej nazwie!\n")

bank = odczyt_banku.odczytaj_z_dysku()  #utworzenie obiektu bank na podstawie pliku przy pomocy metody odczytaj_z_dysku obiektu odczyt_banku
bank.raport_wszystkie()             #wywołanie metody raport_wszystkie obiektu bank klasy Bank
