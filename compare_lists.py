import math


def comp(array1, array2):
    if array2 is None or array1 is None:
        return False
    elif len(array1) == 0 and len(array2) == 0:
        return True
    else:
        for elem in array1:
            for element in array2:
                if elem * elem in array2 and math.sqrt(element) in array1:
                    continue
                else:
                    return False
    return True


print(comp([121, 144, 19, 161, 19, 144, 19, 11], [121, 14641, 20736, 36100, 25921, 361, 20736, 361]))