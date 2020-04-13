def factors(n):
    return [i for i in range(2, n//2 + 1) if n % i == 0]

def proper_fractions(n):
    res = []
    for i, j in [(i, j) for i in factors(n) for j in [i for i in range(1, n) if i not in factors(n)] if j % i == 0]:
        res.append(i)
        res.append(j)
    return len([f"{i}/15" for i in range(1, n) if i not in list(set(res))])

print(proper_fractions(1))
# def proper_fractions(n):
#     phi = n > 1 and n
#     for p in range(2, int(n ** .5) + 1):
#         if not n % p:
#             phi -= phi // p
#             while not n % p:
#                 n //= p
#     if n > 1:
#         phi -= phi // n
#     return phi