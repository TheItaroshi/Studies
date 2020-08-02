nazwa_pliku = input("Podaj nazwę pliku, który chcesz otworzyć: ")

with open(nazwa_pliku) as plik:
    line = plik.readlines()
    print(line)