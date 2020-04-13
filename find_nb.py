def find_nb(m):
    n = 1
    total = n**3
    while True:
        if total == m:
            return n
        elif total > m:
            return -1
        n += 1
        total += n ** 3


print(find_nb(135440716410000))