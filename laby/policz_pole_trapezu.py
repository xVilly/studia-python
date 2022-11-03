def pole_trapezu(a, b, h):
    try:
        return (a+b)*h/2.
    except:
        return 0.

print(pole_trapezu(input('Podaj a: '), input('Podaj b: '), input('Podaj h: ')))