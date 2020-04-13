from itertools import permutations as perm


def permutations(string):
    perm_list = perm(string)
    return set(["".join(i) for i in perm_list])


print(permutations("hell"))
