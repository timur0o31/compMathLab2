def secant(func, a, b,epsilon):
    iteration = 0
    x1 = a
    x0 = b
    while abs(x1 - x0) >= epsilon:
        x_new = x1 - (x1 - x0) * func(x1) / (func(x1) - func(x0))
        x0, x1 = x1, x_new
        iteration += 1
        if abs(func(x1)) <= epsilon:
            break
    return x1, func(x1), iteration