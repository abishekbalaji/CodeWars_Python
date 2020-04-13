from math import sqrt


def fibo(r):
    num1 = 0
    num2 = 1
    num3 = num1 + num2
    fib_list = [0, 1, num3]
    while num3 <= r:
        num1 = num2
        num2 = num3
        num3 = num1 + num2
        fib_list.append(num3)
    return fib_list


def product_fib(prod):
    l = fibo(sqrt(prod))
    result = None
    for i in range(len(l) - 1, 0, -1):
        if l[i] * l[i - 1] == prod:
            return [l[i-1], l[i], True]
    if result is None:
        fibo_list = fibo(prod)
        for i in range(1, len(fibo_list)):
            if fibo_list[i - 1] * fibo_list[i] > prod:
                result = [fibo_list[i - 1], fibo_list[i], False]
                break
    return result

print(product_fib(5895))


def productFib(prod):
    a, b = 0, 1
    while prod > a * b:
        a, b = b, a + b
    return [a, b, prod == a * b]

