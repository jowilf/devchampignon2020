import itertools

db6 = [10, 27, 28, 8, 5, 3, 12, 18, 22, 4, 23, 15, 20, 13, 29, 19, 2, 1, 21, 24, 26, 17, 11, 7, 25, 6, 14, 9, 16, 0]


def rf6(s):
    r = ['a'] * 30
    for i in range(30):
        r[db6[i]] = s[i]
    return "".join(r)


def rf2(s):
    r = ['a'] * 30
    for i in range(30):
        if i % 2 == 0:
            r[i] = s[i // 2]
        else:
            r[i] = s[15 + (i - 1) // 2]
    return "".join(r)


def rf1(s):
    return f1(s)


def f1(s):
    return s[::-1]


def f2(s):
    return s[::2] + s[1::2]


def f3(s):
    r = ''
    for c in s:
        r += chr(ord(c) ^ 0xf)
    return r


def rf3(s):
    return f3(s)


def f4(s):
    r = ''
    for c in s:
        r += chr(ord(c) - 1 if ord(c) != 32 else 126)
    return r


def rf4(s):
    return f5(s)


def f5(s):
    r = ''
    for c in s:
        r += chr(ord(c) + 1 if ord(c) != 126 else 32)
    return r


def rf5(s):
    r = ''
    for l in s:
        r += chr(ord(l) - 1 if ord(l) != 32 else 126)
    return r


def f6(s):
    r = ''
    idx = 1
    for i in range(30):
        idx *= 11
        idx %= 31
        r += s[idx - 1]
    return r


def rf7(s):
    return s.swapcase()


def f7(s):
    return s.swapcase()


def f8(s):
    r = ''
    for c in s:
        if 'a' <= c <= 'z':
            r += chr((ord(c) - ord('a') + 13) % 26 + ord('a'))
        else:
            r += c
    return r


def rf8(s):
    r = ''
    for l in s:
        if 'a' <= l <= 'z':
            r += chr((ord(l) - ord('a') - 13) % 26 + ord('a'))
        else:
            r += l
    return r


def f9(s):
    r = ''
    for c in s:
        if 'A' <= c <= 'Z':
            r += chr((ord(c) - ord('A') + 13) % 26 + ord('A'))
        else:
            r += c
    return r


def rf9(s):
    r = ''
    for c in s:
        if 'A' <= c <= 'Z':
            r += chr((ord(c) - ord('A') - 13) % 26 + ord('A'))
        else:
            r += c
    return r


def rf10(s):
    return s[1:] + s[0]


def f10(s):
    return s[-1] + s[:-1]


def check(s):
    if len(s) != 30 or 'XHFS%~p8#j:&ih<jim~NYFj5i!oEX%' != f6(f6(f2(f1(f7(f10(f5(f5(f6(f7(f6(f8(f2(f9(f8(f6(f5(f6(f2(f6(
            f7(f3(f3(f5(f2(f2(f2(f8(f2(f1(f10(f4(f8(f5(f5(
                f8(f2(f9(f2(f5(f3(f7(f8(f3(f4(f5(f10(f4(f1(f9(s)))))))))))))))))))))))))))))))))))))))))))))))))):
        print('Nope')
    else:
        print('OK!')


rep = (rf9(rf1(rf4(rf10(rf5(rf4(rf3(rf8(rf7(rf3(rf5(rf2(rf9(rf2(rf8(
    rf5(rf5(rf8(rf4(rf10(rf1(rf2(rf8(rf2(rf2(rf2(rf5(rf3(rf3(rf7(
        rf6(rf2(rf6(rf5(rf6(rf8(rf9(
            rf2(rf8(rf6(rf7(rf6(rf5(rf5(rf10(rf7(rf1(rf2(rf6(rf6('XHFS%~p8#j:&ih<jim~NYFj5i!oEX%'))))))))))))))))))))
    )))))))))))))))
))))))))))))))))
print(rep)
check(input('Enter the flag: '))
