pesel = input("Podaj numer PESEL: ")

if len(pesel) == 11 and pesel.isdigit():
    poprawnosc = 9*int(pesel[0]) + 7*int(pesel[1]) + 3*int(pesel[2]) + 1*int(pesel[3]) + 9*int(pesel[4]) + 7*int(pesel[5]) + 3*int(pesel[6]) + 1*int(pesel[7]) + 9*int(pesel[8]) + 7*int(pesel[9])

    # Okreslenie roku:

    # Lata 2000-2099
    if int(pesel[2]) == 2 or int(pesel[2]) == 3:
        miesiac = int(pesel[2] + pesel[3]) - 20
        rok = "20" + pesel[0] + pesel[1]
        dzien = pesel[4]+pesel[5]
        if miesiac < 10:
            miesiac = "0" + str(miesiac)
        else:
            miesiac = str(miesiac)
    # Lata 1800-1899
    elif int(pesel[2]) == 8 or int(pesel[2]) == 9:
        miesiac = int(pesel[2] + pesel[3]) - 80
        rok = "18" + pesel[0] + pesel[1]
        dzien = pesel[4] + pesel[5]
        if miesiac < 10:
            miesiac = "0" + str(miesiac)
        else:
            miesiac = str(miesiac)
    # Lata 2100-2199
    elif int(pesel[2]) == 4 or int(pesel[2]) == 5:
        miesiac = int(pesel[2] + pesel[3]) - 40
        rok = "21" + pesel[0] + pesel[1]
        dzien = pesel[4] + pesel[5]
        if miesiac < 10:
            miesiac = "0" + str(miesiac)
        else:
            miesiac = str(miesiac)
    # Lata 2200-2299
    elif int(pesel[2]) == 6 or int(pesel[2]) == 7:
        miesiac = int(pesel[2] + pesel[3]) - 60
        rok = "22" + pesel[0] + pesel[1]
        dzien = pesel[4] + pesel[5]
        if miesiac < 10:
            miesiac = "0" + str(miesiac)
        else:
            miesiac = str(miesiac)
    else:
        miesiac = pesel[2] + pesel[3]
        rok = "19"+ pesel[0] + pesel[1]
        dzien = pesel[4] + pesel[5]

    # Okreslenie plci:
    if int(pesel[9]) % 2 == 0:
        plec = "K"
    else:
        plec = "M"

    przystepny = False

    big = (1,3,5,7,8,10,12)
    if (int(rok) % 4 == 0 and int(rok) % 100 != 0) or int(rok) % 400 == 0:
        przystepny = True

    dzien_test = False

    if (int(dzien) > 0) and (int(dzien) < 32) and int(miesiac) in big:
        dzien_test = True
    elif (int(dzien) > 0) and (int(dzien) < 31) and (int(miesiac) in big) == False:
        dzien_test = True
    elif ((int(dzien) > 0) and (int(dzien) < 30) and przystepny) or ((int(dzien) > 0) and (int(dzien) < 29) and (przystepny == False)):
        dzien_test = True
    else:
        dzien_test = False

    miesiac_test = False

    if (int(miesiac) > 0 and int(miesiac) < 13):
        miesiac_test = True

    if int(pesel[10]) == poprawnosc % 10:
        if dzien_test and miesiac_test:
            print(dzien + "-" + miesiac + "-" + rok, plec)
        else:
                print("BŁĘDNY NUMER PESEL")
    else:
            print("BŁĘDNY NUMER PESEL")
else:
    print("BŁĘDNY NUMER PESEL")