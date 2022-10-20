
def policz_max():
    ilosc_liczb = 0
    try:
        ilosc_liczb = int(input('Podaj ilosc liczb ktore wprowadzisz: '))
        if ilosc_liczb < 1:
            print('Musisz wprowadzic conajmniej jedna liczbe')
            return
        max = float(input('Podaj liczbe: '))
        c = 1
        while c < ilosc_liczb:
            liczba = float(input('Podaj liczbe: '))
            if liczba > max:
                max = liczba
            c += 1
        print(f'Z wszystkich podanych liczb najwieksza byla {max}')
    except:
        print('Wprowadzono niepoprawna liczbe')
        return

policz_max()

