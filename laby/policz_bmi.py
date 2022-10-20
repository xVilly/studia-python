
def policz_bmi():
    waga = wzrost = 0
    try:
        waga = float(input('Podaj wage w kg: '))
    except:
        print('Podano zla wage!')
        return

    try:
        wzrost = float(input('Podaj wzrost w cm: '))
    except:
        print('Podano zly wzrost!')
        return

    if waga > 0 and wzrost > 0:
        bmi = waga / ((wzrost/100)**2)
        print(f'Twoje BMI wynosi {round(bmi, 2)}')
    else:
        print('Waga i wzrost musza byc wieksze od zera')
        return

policz_bmi()
