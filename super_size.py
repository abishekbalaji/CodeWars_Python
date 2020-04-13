def super_size(n):
    res = list(str(n))
    res.sort(reverse=True)
    temp = ""
    return int(temp.join(res))

super_size(1234)
