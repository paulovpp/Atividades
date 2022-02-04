# Class 4 - Derivatives
# Dec 09, 2021


from sympy import * 
# import numpy as np
# import matplotlib.pyplot as plt

x, f, g, h, j, ll, m, n, p, q = symbols("x f g h j ll m n p q", real=True)


def calc_derivative(eq, variable, rank):
    """
    To calculate derivatives of any function
    """
    return diff(eq, variable, rank)


if __name__ == '__main__':
    init_printing()
    g = -2*x**3 - 4*x**2 + 13*x - 1
    h = 2 * x + ln(x)
    j = sin(x)
    ll = tan(x)
    m = sin(x)*cos(x)
    n = sqrt(x**2 - 5*x)
    p = (3*x**2 - 4*x) / (2*x**3 + 6)

    # calculating the first derivatives

    print(calc_derivative(g, x, 1))
    print(calc_derivative(h, x, 1))
    print(calc_derivative(j, x, 1))
    print(calc_derivative(ll, x, 1))
    print(calc_derivative(m, x, 1))
    print(calc_derivative(n, x, 1))
    print(calc_derivative(p, x, 1))

    # calculating the second derivatives

    print(calc_derivative(g, x, 2))
    print(calc_derivative(h, x, 2))
    print(calc_derivative(j, x, 2))
    print(calc_derivative(ll, x, 2))
    print(calc_derivative(m, x, 2))
    print(calc_derivative(n, x, 2))
    print(calc_derivative(p, x, 2))
    print()

    # calculating maximum and minimum
    # 1st derivative = price
    # 2nd derivative = profit

    q = -4*x**2 + 4000*x - 200000
    d1 = calc_derivative(q, x, 1)
    price = solve(Eq(d1, 0))
    profit = q.subs(x, price[0])

    d2 = calc_derivative(q, x, 2)

    print(f'Price: {price}')
    print(f'Profit: {profit}')
