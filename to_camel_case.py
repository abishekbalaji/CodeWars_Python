def to_camel_case(text):
    l = [x for x in text]
    if text == "":
        return ""
    else:
        for i in range(len(l)):
            if l[i] == '-' or l[i] == '_':
                l[i+1] = l[i+1].capitalize()
        return "".join(l).replace("_", "").replace("-", "")

print(to_camel_case("the-stealth-warrior"))