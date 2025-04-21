def newton(func,x0,epsilon,func_derivative):
    count_iteration = 0
    while True:
        x1 = x0 - (func(x0)/func_derivative(func,x0))
        count_iteration += 1
        if (abs(x1-x0) <= epsilon or abs(func(x1)/func_derivative(func,x1)) <= epsilon) and abs(func(x1)) <= epsilon:
            break
        x0 = x1
    return x1, count_iteration
