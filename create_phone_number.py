def create_phone_number(n):
    l = []
    for i in n:
        l.append(str(i))
    l = ''.join(l)
    return f"({l[0:3]}) {l[3:6]}-{l[6:]}"


print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
