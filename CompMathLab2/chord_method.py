def chord_method(func, a, b,epsilon):
    iteration = 0
    while abs(b - a) >= epsilon:
        x = a - (b-a)*func(a)/(func(b) - func(a))
        if func(a)*func(x)>0:
            a = x
        else:
            b = x
        if abs(func(x)) <= epsilon:
            break
        iteration += 1
    return x, func(x), iteration