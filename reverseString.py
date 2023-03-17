def reverseString(s):
    # r = s[::-1]
    # return r

    # r = list(reversed(s))
    # return r

    r = list()
    for i in s:
        r = [i] + r
    return r



print(reverseString(["a","b","c"]))