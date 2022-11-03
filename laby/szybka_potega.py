from policz_silnie import silnia
from math import factorial


def policz(x, n):
    if (n == 0):
        return 1
    if (n % 2 == 0):
        p = policz(x, n//2)
        return p*p
    else:
        p = policz(x, n//2)
        return p*p*x

def policz_petla(x, n):
    w = 1
    while n != 0:
        if n%2 == 1:
            w *= x
        x = x * x
        n //= 2
    return w



def policz_pot(x, eps):
    suma = 0
    a = 1
    i = 0
    _l = 1
    _m = 1
    while abs(a) >= eps:
        _ll = _l*x
        _mm = _m*max(i,1)
        a = (_ll)/(_mm)
        _l = _ll
        _m = _mm
        i += 1
        suma += a
    return suma

print(policz_pot(1, 0.0000000000000000000000000001))
