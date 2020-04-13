num_str_dict = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
                "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15, "sixteen": 16,
                "seventeen": 17, "eighteen": 18, "nineteen": 19, "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50,
                "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90, "hundred": 100, "thousand": 1000,
                "million": 1000000, "and": 1}


def parse_int(string):
    string = string.replace(" and ", " ")
    print(string)
    l = string.split(" ")
    lr = []
    result = []
    y = []
    for i in range(0, len(l), 2):
        lr.append(l[i: i+2])
    print(lr)
    for i in lr:
        for j in i:
            try:
                if j.index("-"):
                    k = j.split("-")
                    m = [num_str_dict[x] for x in k]
                    result.append(sum(m))
            except ValueError:
                y.append(num_str_dict[j])
        if len(y) > 1:
            result.append(y[0] * y[1])
            y.clear()
        elif len(y) == 1:
            result.append(y[0])
    return sum(result)


print(parse_int('three hundred and twenty-six thousand eight hundred and sixteen'))
