def suma_bomb(plansza, a, b):
    from pobierz_element import pobierz_element

    suma = 0

    if pobierz_element(plansza, a-1, b-1) == "*":
        suma += 1
    else:
        pass
    if pobierz_element(plansza, a-1, b) == "*":
        suma += 1
    else:
        pass
    if pobierz_element(plansza, a-1, b+1) == "*":
        suma += 1
    else:
        pass
    if pobierz_element(plansza, a, b-1) == "*":
        suma += 1
    else:
        pass
    if pobierz_element(plansza, a, b+1) == "*":
        suma += 1
    else:
        pass
    if pobierz_element(plansza, a+1, b-1) == "*":
        suma += 1
    else:
        pass
    if pobierz_element(plansza, a+1, b) == "*":
        suma += 1
    else:
        pass
    if pobierz_element(plansza, a+1, b+1) == "*":
        suma += 1
    else:
        pass
    if pobierz_element(plansza, a, b) == "*":
        suma = "*"
    return suma

# plansza = ["**...",
#            ".....",
#            ".*..."]
#
# assert suma_bomb(plansza, 1, 0) == 3
# assert suma_bomb(plansza, 0, 2) == 1
# assert suma_bomb(plansza, 1, 4) == 0
# assert suma_bomb(plansza, 2, 1) == 0
# assert suma_bomb(plansza, 1, 2) == 2
# assert suma_bomb(plansza, 1, 1) == 3
# assert suma_bomb(plansza, 2, 0) == 1
