def excelTitleToNumber(columnNumber):
    title = ""
    while columnNumber > 0:
        columnNumber -= 1
        title = chr(columnNumber % 26 + 65) + title
        columnNumber //= 26
    return title
print(excelTitleToNumber(701))