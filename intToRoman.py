def romanToInteger(num):
    total = ''
    dic = {
        'I': 1,
        'IV': 4,
        'V': 5,
        'IX': 9,
        'X': 10,
        'XL': 40,
        'L': 50,
        'XC': 90,
        'C': 100,
        'CD': 400,
        'D': 500,
        'CM': 900,
        'M': 1000
    }

    for i, val in reversed(dic.items()):
        if num // val:
            count = num // val
            print(i, count, i*count)
            total += (i*count)
            num = num % val
    return total

print(romanToInteger(2000))


