def plusOne(digits):
    strings = ""
    for number in digits:
        strings += str(number)
        #print(strings)

    temp = str(int(strings) + 1)

    return [int(temp[i]) for i in range(len(temp))]
print(plusOne([1,2,3]))