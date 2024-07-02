# Created 1st July, 2024
# Huge credits to Adeala Adegbulugbe - copied 75% from his work


def Dfx(f, x, precision=15):
    dx = 5 * pow(10, -precision)
    return (f(x + dx) - f(x - dx)) / (2 * dx)


def bisection_method(f, precision=5, a=-100, b=100):
    PRECISION_LIMIT = 5 * pow(10, -precision)

    while True:
        xr = (a + b) / 2
        fa = f(a)
        fb = f(b)
        fxr = f(xr)

        if abs(fa * fxr) <= PRECISION_LIMIT:
            return xr
        elif fa * fxr < 0:
            b = xr
        elif fa * fxr > 0:
            a = xr


def newton_raphson_method(f, x=2, precision=5):
    xn = x
    PRECISION_LIMIT = 5 * pow(10, -precision)

    while True:
        xn_plus_one = xn - (f(xn) / Dfx(f, xn))

        if abs(f(xn_plus_one)) <= PRECISION_LIMIT:
            return xn_plus_one

        xn = xn_plus_one


def str_to_func(string):
    def f(x):
        return eval(string)

    return f


if __name__ == "__main__":
    f1 = str_to_func("(x ** 3) - x - 1")
    f2 = str_to_func("(x ** 3) - (2 * x) - 5")

    print(f"For the first function, x^3 - x - 1")
    print("----------\n")
    res = bisection_method(f1)
    print(f"Bisection method gives {res}")

    res = newton_raphson_method(f1)
    print(f"Newton-Raphson gives {res}")

    print("\n\n")

    print(f"For the second function, x^3 - 2x - 5")
    print("----------\n")
    res = bisection_method(f2)
    print(f"Bisection method gives {res}")

    res = newton_raphson_method(f2)
    print(f"Newton-Raphson gives {res}")
