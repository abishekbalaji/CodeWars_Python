import math
def primeFactors(n):
    prime_list = getPrime(n)
    prime_dict = {}
    for x in prime_list:
        prime_dict[f'{x}'] = 0
    for x in prime_list:
        while n % x == 0:
            prime_dict[f'{x}'] += 1
            n = n // x
            if prime_check(n):
                prime_dict[f'{n}'] = 1
                n = n // x
    result = ""
    for x, y in prime_dict.items():
        if y == 1:
            result += f"({x})"
        if y > 1:
            result += f"({x}**{y})"
    return result


def getPrime(n):
    flag = 0
    prime = [2]
    r = int(math.sqrt(n)) + 10
    for i in range(3, r):
        for j in range(2, i // 2 + 2):
            if i % j == 0:
                flag = 1
                break
        if flag == 0:
            prime.append(i)
        flag = 0
    return prime

def prime_check(n):
    flag = 0
    for i in range(2, int(math.sqrt(n) + 10)):
        if n % i == 0:
            flag = 1
            break
    if flag == 0:
        return True

print(primeFactors(7919))



