def numberToHex(num):
    if num < 0:
        num += 2 ** 32
    ans = ("%x" % num)


numberToHex(-1)