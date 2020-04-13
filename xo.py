def xo(s):
    s = s.lower()
    xcount = 0
    ocount = 0
    for i in s:
        if i == 'x':
            xcount += 1
        elif i == 'o':
            ocount += 1
    if xcount == ocount:
        return True
    elif xcount != ocount:
        return False

s = "efsjdno"
print(xo(s))