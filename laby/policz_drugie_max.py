
def policz_drugie_max():
    ilosc_liczb = 0
    try:
        ilosc_liczb = int(input('Podaj ilosc liczb ktore wprowadzisz: '))
        if ilosc_liczb < 2:
            print('Musisz wprowadzic conajmniej jedna liczbe')
            return
        
        max = float(input('Podaj liczbe: '))
        drugie_max = max
        c = 1
        while c < ilosc_liczb:
            liczba = float(input('Podaj liczbe: '))
            if liczba > max:
                o_max = max
                max = liczba
                if max != drugie_max:
                    drugie_max = o_max
            c += 1
        print(f'Z wszystkich podanych liczb najwieksza byla {max}')
        if drugie_max == max:
            print('Drugie maximum nie istnieje')
        else:
            print(f'Drugim maximum jest liczba {drugie_max}')
    except:
        print('Wprowadzono niepoprawna liczbe')
        return

policz_drugie_max()

