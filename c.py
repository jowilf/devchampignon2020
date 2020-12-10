def rotate(input, d):
    # slice string in two parts for left and right
    Lfirst = input[0: d]
    Lsecond = input[d:]
    Rfirst = input[0: len(input) - d]
    Rsecond = input[len(input) - d:]
    return Rsecond + Rfirst
    # now concatenate two parts together
    # print("Left Rotation : ", (Lsecond + Lfirst))
    # print("Right Rotation : ", (Rsecond + Rfirst))


a = '10001000001011101101000111000001001011000011001101010000101101110110111100111111110100011010111001111000011001001011111101001110011111111101011111000111001110100110111011011101010011011101101111101011011 '
chunks, chunk_size = len(a), len(a) // 29
t = [a[i:i + chunk_size] for i in range(0, chunks, chunk_size)]
t.pop()
i = 0
print(t)
for j in range(len(t)):
    val = t[j]
    t[j] = rotate(val, i)
    print(val, t[j], i)
    i = (i + 1) % 8
print(t)
pow
tt = list(map(lambda v: int(v, 2), t))
ttt = "".join(map(chr, tt))
print(list(map(lambda v: int(v, 2), t)))
print(ttt)
