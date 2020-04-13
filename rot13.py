alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def rot13(message):
    new_str = ''
    for i in range(len(message)):
        try:
            index = alpha.index(message[i].lower()) + 13
        except ValueError:
            new_str += message[i]
        else:
            if index >= 26:
                index -= 26
            new_str += alpha[index]
    if message.islower():
        return new_str
    elif message.isupper():
        return new_str.upper()
    else:
        return new_str.capitalize()


print(rot13("Test"))

