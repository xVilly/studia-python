def policz(n):
    a = 1
    b = 1
    for i in range(3, n+1):
        c = a
        a = b
        b = a+c
    if n+1 < 3:
        return 1
    else:
        return a+b

for i in range(0, 10000):
    print(f'{i}\t{policz(i)}')
