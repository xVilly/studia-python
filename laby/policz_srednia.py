
def policz_srednia():
    suma_ocen = 0
    ilosc_ocen = 0

    print('Podaj oceny do wyliczenia sredniej. Wprowadz \'stop\' aby zakonczyc wprowadzanie.')

    while True:
        ocena = 0
        try:
            ocena = input(f'Podaj ocene: ')
            ocena_int = int(ocena)
            if ocena_int > 0 and ocena_int < 7:
                suma_ocen += ocena_int
                ilosc_ocen += 1
            else:
                print('Podana ocena jest poza skala. Zostanie ona pominieta.')
        except:
            if ocena == 'stop':
                if ilosc_ocen < 1:
                    print('Musisz podac conajmniej jedna ocene')
                    return
                print(f'Srednia wynosi {round(suma_ocen/ilosc_ocen, 2)}')
                return
            else:
                print('Podana ocena jest niepoprawna. Zostanie ona pominieta.')

policz_srednia()

