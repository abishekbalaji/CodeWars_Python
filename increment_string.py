def increment_string(strng):
    print(strng)
    if strng == "":
        return str(1)
    else:
        digit = -999
        digit_start = -999
        first_len = -999
        for i in range(len(strng)):
            if strng[i].isdigit():
                first_len = len(strng[i:])
                print(strng[i:])
                digit = int(strng[i:])
                digit_start = i
                break
        if digit == -999:
            strng += str(1)
        else:
            digit += 1
            if len(str(digit)) != first_len:
                dif = first_len - len(str(digit))
                strng = strng[:digit_start] + str(0) * dif + str(digit)
            else:
                strng = strng[:digit_start] + str(digit)
        return strng


print(increment_string("m5c7-so439115"))