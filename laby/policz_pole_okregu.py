pi = 3.1415

def pole_kola(r):
    try:
        return pi * float(r)**2
    except:
        return 0

print(pole_kola(input('Podaj obwod kola: ')))