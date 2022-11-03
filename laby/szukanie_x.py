# dzielenie przedzialu funkcji na polowy, w poszukiwaniu miejsca zerowego (porownywanie znakow dwoch koncow przedzialu)
import math

pi = math.pi

def f(x):
    return math.sin(x)


def znajdz_zerowe(f, x1, x2, eps):
    if x1 > x2:
        _t = x2
        x2 = x1
        x1 = _t
    m = 0
    while abs(x1 - x2) >= eps:
        print(f"{x1}, {x2}, {m}")
        if f(x1) == 0:
            return x1
        elif f(x2) == 0:
            return x2
        m = (x1 + x2)/2
        if f(m) == 0:
            return m
        if f(x1) * f(m) < 0:
            x2 = m
            continue
        elif f(m) * f(x2) < 0:
            x1 = m
            continue
    return m

print(znajdz_zerowe(f, 0.9*pi, 22.5*pi, 0.00000001)/pi)
