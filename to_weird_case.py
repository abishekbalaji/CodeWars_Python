def to_weird_case(string):
    l = string.split(" ")
    strf = ""
    for i in l:
        for j in range(len(i)):
            if j % 2 == 0:
                strf += i[j].capitalize()
            else:
                strf += i[j]
        if len(l) > 1 and i is not l[-1]:
            strf += " "
    return strf


to_weird_case("hello world")
