def count_ones(left, right):
    res = 0
    for i in range(left, right + 1):
        res += bin(i)[2:].count("1")
    return res

print(count_ones(4,7))