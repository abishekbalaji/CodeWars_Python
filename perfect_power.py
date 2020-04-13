from math import sqrt
def something(big, small):
    q = big / small
    count = 1
    while q >= small:
        q = q / small
        if q != int(q) or (q < small and q != 1):
            return False
        count += 1
    return count
def isPP(n):
    num = n
    count = 1
    l = [i for i in range(2, int(sqrt(n)) + 1) if n % i == 0]
    result_list = []
    for i in l:
        result = something(n, i)
        if result != False:
            elem = i
        result_list.append(result)
    print(result_list)
    for elam in result_list:
        if type(elam) is int:
            return f"{n} = {elem}^{elam}"
    return f"{n} isn't a perfect power"

print(isPP(100))



