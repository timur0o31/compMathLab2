def half_division(func,a,b,epsilon):
    n = 0
    while abs(a-b)>epsilon:
        x = (a+b)/2
        if func(a) * func(x)>0:
            a = x
        else:
            b = x
        if abs(func(x))<=epsilon:
            break
        n += 1
    return x, func(x), n

