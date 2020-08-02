try:
    with open("lista.txt", "a+") as lista:
        lista_studentow = []
        for linia in lista:
            lista_studentow.append(linia)
            print(linia.strip())

        print("\nDodaj nowych studentów\n")

        imie = "tymczasowa"
        while imie != "":
            imie = input("Podaj imię studenta: ")
            if imie != "":
                nazwisko = input("Podaj naswisko studenta: ")
                grupa = input("Podaj grupę studenta: ")
                dane = imie + ";" + nazwisko + ";" + grupa + "\n"
                lista_studentow.append(dane)
                lista.write(dane)

except IOError:
    print("Brak pliku!")
    print("\nDodaj nowych studentów\n")

    with open("lista.txt", "w") as lista:

        imie = "tymczasowa"
        while imie != "":
            imie = input("Podaj imię studenta: ")
            if imie != "":
                nazwisko = input("Podaj naswisko studenta: ")
                grupa = input("Podaj grupę studenta: ")
                dane = imie + ";" + nazwisko + ";" + grupa + "\n"
                lista_studentow.append(dane)
                lista.write(dane)

