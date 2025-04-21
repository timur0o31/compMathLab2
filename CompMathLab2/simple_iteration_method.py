def simple_iterations(func,phi,x0,epsilon,max_iterations = 1000):
    count_iterations = 0
    while True:
        count_iterations += 1
        x=phi(x0)
        if abs(x - x0) <= epsilon and abs(func(x)) <= epsilon:
            break
        if count_iterations >= max_iterations:
            return None, None, count_iterations
        x0 = x
    return x,func(x), count_iterations

def simple_iterations_for_system_of_equations(phi1,phi2,x1,y1,epsilon, max_itr=1000):
    count_iterations = 0
    while True:
        x_new = phi1(x1, y1)
        y_new = phi2(x1, y1)
        count_iterations += 1
        if abs(x_new - x1) < epsilon and abs(y_new - y1) < epsilon:
            break
        if count_iterations >= max_itr:
            print("Не удалось вычислить корень системы в пределе 1000 итераций.")
            break
        x1, y1 = x_new, y_new
    return x_new, y_new, count_iterations