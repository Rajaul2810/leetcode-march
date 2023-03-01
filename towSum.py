def towSum(num1 , num):
    prevMap = {}
    for i , value in enumerate(num1):
        number = num - value
        if number in prevMap:
            return [prevMap[number],i]
        else:
             prevMap[value]=i


towSum([3,2,4], 6)