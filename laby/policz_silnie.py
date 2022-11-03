def silnia(n):
    x = 1
    y = 2
    i = 2
    while i < n:
        z = x * y
        i += 1
        x = z
        y = i
    if n > 0:
        return x * y
    else:
        return 1

