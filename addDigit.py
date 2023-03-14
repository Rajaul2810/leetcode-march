def addDigits(num):
    if num == 0:
        return num
    elif num % 9 == 0:
        return 9
    else:
        return (num % 9)
print(addDigits(38))
for i in range(2,3):
    print(i)