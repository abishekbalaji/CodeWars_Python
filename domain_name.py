import re


def domain_name(url):
    text = ""
    for i in range(len(url)):
        if url[i] == '/' or url[i] == '.':
            text = url[i:]
            break
    return text


print(domain_name("http://www.google.com"))
