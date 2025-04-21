from matplotlib import pyplot as plt
import numpy as np
from math import e,sin,cos
from half_division_method import half_division
from newton_method import newton
from chord_method import chord_method
from secant_method import secant
from simple_iteration_method import *
def verification(func, a,b,x0, epsilon):
    if func(a)*func(b) < 0:
        x = a
        x_val=[]
        while x<b:
            x_val.append(x)
            x += epsilon
        deriv_val = [derivative(func,x,epsilon) for x in x_val]
        if all(d>0 for d in deriv_val) or all(d<0 for d in deriv_val):
            return True
    return False
"""
def jacobi(func1, func2, a, b, x0, epsilon):
    df1_dx = part_derivative()
    df2_dx =
    df1_dy =
    df2_dy =
    return df1_dx * df2_dy - df1_dy * df2_dx
"""
def part_derivative(func,x,y,var, h=0.00001):
    if var == 'x':
        return (func(x + h, y) - func(x, y)) / h
    else:
        return (func(x, y + h) - func(x, y)) / h


def derivative(func,x,dx = 0.00001):
    return (func(x+dx) - func(x))/dx
def eps():
    epsilon = 0.001
    while True:
        try:
            epsilon = float(input("Введите значение эпсилона: "))
            if epsilon <= 0:
                raise Exception("Значение эпсилона не может быть отрицательным!")
            if epsilon > 1:
                raise Exception("Значение эпсилона не может быть больше 1!")
            break
        except ValueError:
            print("Введите число!")
        except Exception as e:
            print(e)
    return epsilon

def graph(func,a,b,x,epsilon):
    args=[]
    vals=[]
    x1=a
    while x1<b:
        args.append(x1)
        vals.append(func(x1))
        x1 += epsilon
    plt.xlabel("x")
    plt.ylabel("y")
    plt.plot(args,vals,'g')
    plt.annotate("x",xy=(x,func(x)))
    plt.plot([a,b],[0,0],"b")
    plt.show()
def graph_system(func1,func2, x1,y1):
    x = np.linspace(-4, 4,1600)
    y = np.linspace(-4,4,1600)
    X,Y = np.meshgrid(x,y)
    Z1 = np.zeros_like(X)
    Z2 = np.zeros_like(X)
    for i in range(X.shape[0]):
        for j in range(Y.shape[0]):
            Z1[i, j] = func1(X[i, j], Y[i, j])
            Z2[i, j] = func2(X[i, j], Y[i, j])
    plt.annotate('x', xy=(x1, y1))
    plt.contour(X, Y, Z1, levels=[0], colors='r')
    plt.contour(X, Y, Z2, levels=[0], colors='g')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

def solve_linear():
    print("Доступные уравнения:")
    equations = ["1) x³-x+4","2) x³+2,64x²-5,41x¹-11,76","3) x⁵-7x³-12x²+6x+36","4) 4.45*x³+7.81x²-9.62x-8.17 ","5) e**sin(x)+x⁷-8"]
    for equation in equations:
        print(equation)
    print("Введите номер выбранного вами уравнения")
    while True:
        try:
            case=input("Выберите номер уравнения: ").strip()
            if case not in ['1', '2', '3', '4', '5']:
                raise Exception
            else:
                case = int(case)
                break
        except ValueError:
            print("Номер должен быть целым числом")
        except Exception:
            print("Номер должен лежать в промежутке [1,5]")
    match case:
        case 1:
            equation = lambda x: x ** 3 - x + 4
            phi = lambda x: np.cbrt(x - 4)
        case 2:
            equation = lambda x: x ** 3 + 2.64 * x ** 2 - 5.41 * x - 11.76
            phi = lambda x: (x**3+2.64*x**2-11.76)/5.41
        case 3:
            equation = lambda x: x**5-7*x**3-12*x**2+6*x-11.76
            phi = lambda x: (7*x**3+12*x**2-6*x+11.76)/x**4
        case 4:
            equation = lambda x: 4.45*x**3+7.81*x**2-9.62*x-8.17
            phi = lambda x: (4.45*x**3+7.81*x**2-8.17)/9.62
        case 5:
            equation = lambda x: e**sin(x)+x**7-8
            phi = lambda x: (8-e**sin(x))**(1/7)

    print("Установите интервал изоляции корней")
    a,b = 0, 0
    epsilon=0
    while True:
        while True:
            print("Введите значения a и b через пробел")
            try:
                a,b = map(float, input().split())
                if (a >= b):
                    print(f'{a} >= {b}. Пожалуйста, введите a < b')
                    continue
                break
            except ValueError:
                print("Введите числа.")
                continue
        if epsilon==0:
            epsilon = eps()
        x0 = (a+b)/2 # начальное приближение
        if not verification(equation,a,b,x0,epsilon):
            print("Данный интервал не удовлетворяет условию единственности корня на отрезке")
            continue
        break
    methods = ["1. Метод половинного деления","2. Метод Ньютона","3. Метод простой итерации"]
    print("Методы вычислений: ")
    for method in methods:
        print(method)
    while True:
        try:
            ans = int(input("Введите номер выбранного вами метода: ").strip())
            if (ans>0 and ans<4):
                break
            else:
                raise Exception
        except ValueError:
            print("Введите целое число")
        except Exception:
            print("Число должно лежать в [1,3]")

    if ans in [1,2,3]:
        match ans:
            case 1:
                answer = half_division(equation,a,b,epsilon)
                print(f"Корень = {answer[0]}, значение функции в данной точке = {answer[1]}, количество итераций = {answer[2]} ")
                graph(equation,a,b,answer[0],epsilon)
            case 2:
                answer = newton(equation,x0,epsilon,derivative)
                print(f"Корень = {answer[0]}, количество итераций = {answer[1]}")
                graph(equation,a,b,answer[0],epsilon)
            case 3:
                mx_val = 0
                x = a
                while x < b:
                    mx_val = max(mx_val, phi(x))
                    x = x + epsilon
                if mx_val < 1:
                    answer = simple_iterations(equation,phi,a,epsilon)
                    print(f"Корень = {answer[0]}, количество итераций = {answer[2]}")
                    graph(equation,a,b,answer[0],epsilon)
                else:
                    print("Метод простых итераций не выполняется")
            case 4: # методы для самопроверки
                answer = chord_method(equation, a, b, epsilon)
                print(f"Корень = {answer[0]}, значение функции в данной точке = {answer[1]}, количество итераций = {answer[2]} ")
            case 5:
                answer = secant(equation, a, b, epsilon)
                print(f"Корень = {answer[0]}, значение функции в данной точке = {answer[1]}, количество итераций = {answer[2]} ")
    else:
        exit(0)


def solve_system():
    print("Доступные системы уравнений:")
    system_equations = [["sin(y+2)-x-1.5","y+cos(x-2)-0.5"],["0.1*x^2+x+0.2*y^2-0.3","0.2x^2+y+0.1*x*y-0.7"]]
    for i in range(len(system_equations)):
        print(f" {i+1} система:\n \t{system_equations[i][0]}\n\t{system_equations[i][1]}")
    while True:
        try:
            ans = int(input("Введите номер системы: ").strip())
            if (ans==1 or ans==2):
                break
            else:
                raise Exception
        except ValueError:
            print("Введите целое число")
        except Exception:
            print("Введите 1 или 2!")
    match ans:
            case 1:
                func1 = lambda x,y: sin(y+2) - x - 1.5
                func2 = lambda x,y: y + cos(x-2) -0.5
                phi1 = lambda x,y: sin(y+2)-1.5
                phi2 = lambda x,y: 0.5 - cos(x-2)
                a1, b1, a2, b2 = -2, -1, 0.5, 1.5
            case 2:
                func1 = lambda x,y: 0.1*x**2 +x+ 0.2 * y**2 - 0.3
                func2 = lambda x,y: 0.2*x**2 + y+0.1*x*y - 0.7
                phi1 = lambda x,y: 0.3 - 0.1*x**2-0.2*y**2
                phi2 = lambda x,y: -0.2*x**2 - 0.1*x*y+0.7
                a1, b1, a2, b2 = 1.5,2,0,0.5
            case _:
                exit(0)
    print("Метод простых итераций")
    epsilon = eps()
    x0 = (a1+b1)/2
    y0 = (a2+b2)/2
    cur_x = a1
    cur_y = a2
    max_val1 = 0
    max_val2 = 0
    """
    while True:
        while True:
            try:
                a1, b1 = map(float, input("Введите значения a1 и b1 по x: ").split())
                a2, b2 = map(float, input("Введите значения a2 и b2 по y: ").split())
                break
            except ValueError:
                print("Введенные значения должны быть числами!")
                continue
        x0 = (a1 + b1) / 2
        y0 = (a2 + b2) / 2
        if func1(a1, a2) * func1(b1, b2) > 0 or func2(a1, a2) * func2(b1, b2) > 0:
            print("Ошибка: На данном интервале может быть несколько корней или нет корня.")
            print("Пожалуйста, введите заново интервалы изоляции корней")
            continue
        else:
            #Jac(func1, func2, x0, y0, epsilon)
            break
    """        
    while cur_x < b1:
        while cur_y < b2:
            max_val1 = max(max_val1, abs(part_derivative(phi1,cur_x,cur_y,'x')) + abs(part_derivative(phi1,cur_x,cur_y,'y')))
            max_val2 = max(max_val2, abs(part_derivative(phi2, cur_x, cur_y, 'x')) + abs(part_derivative(phi2, cur_x, cur_y, 'y')))
            cur_y += epsilon
        cur_x += epsilon
    if max_val1 >= 1 or max_val2 >= 1:
        print("Метод расходится!")
        exit(0)
    ans = simple_iterations_for_system_of_equations(phi1,phi2,x0,y0,epsilon)
    print(f"x = {ans[0]}, y = {ans[1]}, число итераций = {ans[2]}")
    graph_system(func1,func2, ans[0], ans[1])

def main():
    print("Введите 1, если хотите решить уравнение, 2 для решения системы уравнений")
    while True:
        try:
            a = int(input())
            if a == 1:
                solve_linear()
                break
            elif a==2:
                solve_system()
                break
            else:
                print("Введите 1 или 2!")
        except ValueError:
            print("Введите целое число")
            
main()

