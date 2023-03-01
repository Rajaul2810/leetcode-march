def romanToInteger(str):
    total = 0
    dic = {
        'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000
    }

    for i in str:
        print(dic[i])
        total += dic[i]
    if "IV" in str:
        total -= 2
    if "IX" in str:
        total -= 2
    if "XL" in str:
        total -= 20
    if "XC" in str:
        total -= 20
    if "CD" in str:
        total -= 200
    if "CM" in str:
         total -= 200
    return total

print(romanToInteger('IV'))
