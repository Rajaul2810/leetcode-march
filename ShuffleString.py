def restoreString(s, indices):
    count = ['']*len(s)
    for i, c in enumerate(indices):
        count[c] = s[i]
    return ''.join(count)

print(restoreString('codeleet',[4,5,6,7,0,2,1,3]))