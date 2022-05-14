import math
import sympy as sp
from sympy.utilities.lambdify import lambdify


def find_range(big_range, _f, f_prime, jump):
    list_ = []
    start = big_range[0]

    while start <= big_range[1]:
        if f(start) * f(start + jump) < 0:
            list_.append([start, start + jump])

        if f_prime(start) * f_prime(start + jump) < 0:
            list_.append([start, start + jump])

        start = start + jump
    # print(len(list_))
    # print(list_, "\n")
    return list_


def Bisection_Method(func, _range, epsilon):
    temp = epsilon / (_range[1] - _range[0])
    error = - (math.log(temp)) / math.log(2)
    counter = 0
    flag = 0

    a = _range[0]
    b = _range[1]
    while abs(b - a) > epsilon:
        if counter >= error:
            flag = 1
            break
        counter += 1
        c = (a + b) / 2.0
        if func(a) * func(c) > 0:
            a = c
        else:
            b = c
    if flag == 1:
        print("The root is not found after ", error, " iterations\nThe function is not suitable "
                                                       "for the bisection method")
    else:
        if round(func(c)) == 0:
            print("The number of the iterations for finding the root is ", counter)
            print("The root:")
            print(f'({c:.2f}, {abs(func(c)):.2f})\n\n')


def Newton_Raphson(func, _range, epsilon):
    counter = 1
    x_0 = _range[0]

    while True:
        if abs(func(x_0)) < epsilon:
            print("The number of the iterations for finding the root is ", counter)
            print("The root:")
            print(f'({x_0:.2f}, {abs(func(x_0)):.2f})\n\n')
            break

        if _f_prime(x_0) == 0:
            break

        x_0 = x_0 - func(x_0) / _f_prime(x_0)
        counter += 1


def Secant_Method(func, _range, epsilon):
    end = 80
    x_0 = _range[0]
    x_1 = _range[1]
    counter = 1
    while True:
        if func(x_0) == func(x_1):
            break

        x_2 = x_0 - (x_1 - x_0) * func(x_0) / (func(x_1) - func(x_0))
        x_0 = x_1
        x_1 = x_2
        counter += 1

        if counter > end or x_1 < _range[0] or x_1 > _range[1]:
            break

        if abs(func(x_2)) <= epsilon:
            print("The number of the iterations for finding the root is ", counter)
            print("The root:")
            print(f'({x_2:.2f}, {abs(func(x_2)):.2f})\n\n')
            break


# main


x = sp.symbols('x')
_f = x ** 4 + x ** 3 - 3 * (x ** 2)
_f_prime = _f.diff(x)
f = lambdify(x, _f)
_f_prime = lambdify(x, _f_prime)
_big_range = [-3, 2]


eps = 0.0001
_jump = 0.1
list_ranges = find_range(_big_range, _f, _f_prime, _jump)

while True:
    choice = int(input("Please choose one the the following methods:\n1. Bisection method\n2. Newton-Raphson method"
                       "\n3.Secant method\n"))
    if choice == 1:
        for r in list_ranges:
            Bisection_Method(f, r, eps)
        break

    elif choice == 2:
        for r in list_ranges:
            Newton_Raphson(f, r, eps)
        break

    elif choice == 3:
        for r in list_ranges:
            Secant_Method(f, r, eps)
        break

    else:
        print("wrong choice, try again!")
