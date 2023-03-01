
def checkPalindrom(num):
    rev = 0
    temp = num
    while (num > 0):
        dig = num % 10
        rev = rev * 10 + dig
        num = num // 10
    if (temp == rev):
        return True
    else:
        return False
num = int(input())
print(checkPalindrom(num))

