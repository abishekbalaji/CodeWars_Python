def max_count(string):
    str_list = string.split(" ")
    print(str_list)
    result = []
    print(set(str_list))
    for i in range(len(set(str_list))):
        count = 0
        str1 = str_list[i]
        count += 1
        for j in range(len(str_list)):
            if str_list[j] == str1:
                count += 1
        result.append(count)

    return result


def top_3_words(text):
    return


print(max_count("a a a  b  c c  d d d d  e e e e e"))