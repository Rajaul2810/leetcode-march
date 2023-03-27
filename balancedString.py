def balanced(s):
    ans = prefix = 0
    for c in s:
        if c == "R":
            prefix += 1
        else:
            prefix -= 1
        if not prefix:
            ans += 1
    print(ans)
balanced('RLLRL')