# Zadanie 1

x = int(input("Podaj liczbę: "))

print (x*x)

# Zadanie 2

x = float(input("Podaj szerokość: "))
y = float(input ("Podaj długość: "))

print ("Obwód = ", 2*x+2*y)
print ("Pole = ", x*y)

# Zadanie 3

x = int(input ("Podaj liczbę jajek: "))

while x:
    if x > 60:
        kopy=int(x/60)
        print ("Liczba kop: ", kopy)
        x = x-60*kopy
    elif x > 12:
        tuziny=int(x/12)
        print ("Liczba tuzinów: ", tuziny)
        x = x-12*tuziny
    else:
        print ("Liczba pozostałych jaj: ", x)
        x=x-x

# Zadanie 4

temperatura = float(input("Podaj temeperaturę w celcjuszach: "))
print ("Temperatura w Farenhaitach: ", temperatura*1.8+32)

# Zadanie 5

podstawa = float(input("Podaj podstawę: "))
wysokość = float(input ("Podaj wysokość: "))

print ("Pole trójkąta: ", podstawa*wysokość/2)

# Zadanie 6

liczba = int(input("Podaj liczbę całkowitą: "))
if liczba%2==0:
    print("Liczba parzysta")
else:
    print("Nieparzysta")

# Zadanie 7

wczytana  = input("Podaj liczbę")
dlugosc = len(wczytana)
if dlugosc>1:
    print(wczytana[-2]+wczytana[-1])
else:
    print("0"+wczytana)

# Zadanie 8

calkowita = input("Podaj liczbę: ")
if "." in calkowita:
    print("rzeczywista")
else:
    print ("całkowita")

# Zadanie 9

drzewo = int(input("Podaj drzewo: "))
i=1

while i < drzewo:
    print ("*"*i)
    i +=1

while drzewo>=1:
    print ("*"*drzewo)
    drzewo = drzewo -1

# Zadanie 10

naturalna = int(input("Podaj liczbę naturalną: "))
n = 1
suma = 0
while n<=naturalna:
    suma = suma+n
    n += 1
    print (suma)
