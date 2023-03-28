def decodeMessage( key , message):
    d = dict()
    d[" "] = " "
    c = 97
    for i in key:
        if (i != " "):
            if (i not in d):
                d[i] = chr(c)
                c += 1
    ans = ""
    for i in message: ans += d[i]
    return ans
print(decodeMessage("the quick brown fox jumps over the lazy dog","vkbs bs t suepuv"))