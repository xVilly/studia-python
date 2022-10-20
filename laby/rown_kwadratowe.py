from math import sqrt


def policz_rown_kwadratowe():
    a = b = c = 0

    # wczytanie wspolczynnikow
    try:
        a = float(input('Podaj wsp. a: '))
        b = float(input('Podaj wsp. b: '))
        c = float(input('Podaj wsp. c: '))
    except:
        print('Podano niepoprawne wspolczynniki')
        return

    if a == 0:
        print('Wspolczynnik a nie moze byc rowny 0')
        return

    # liczenie delty
    delta = b**2 - 4*a*c

    # podanie rozwiazania
    if delta > 0:
        x1 = (-b + sqrt(delta)) / 2*a
        x2 = (-b - sqrt(delta)) / 2*a
        print(f'Istnieja dwa rozwiazania rzeczywiste: {x1} oraz {x2}')
    elif delta == 0:
        x = (-b) / 2*a
        print(f'Istnieje jedno rozwiazanie rzeczywiste: {x}')
    else:
        print(f'Podane rownanie nie ma rozwiazan rzeczywistych')

policz_rown_kwadratowe()
