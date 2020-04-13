import re


def name_list(names):
    length_of_list = len(names)
    if length_of_list == 0:
        return ""
    else:
        final_list = []
        for i in range(length_of_list):
            if i == length_of_list - 2:
                final_list.append(f"{names[i]['name']} & {names[i + 1]['name']}")
                line = str(final_list)[1:-1]
                return re.sub('[\']', '', line)
            else:
                final_list.append(names[i]['name'])
                if length_of_list == 1:
                    line = str(final_list)[1:-1]
                    return re.sub('[\']', '', line)


print(name_list([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]))
