from math import floor, ceil
def divideTwoIntegers(dividend,divisor):
    # if divisor==1:
    #     return dividend
    # elif divisor == -1:
    #     return -dividend
    # if divisor < 0 and dividend >0:
    #     divisor = divisor * -1
    #     print(divisor)
    #     sum1 = 0
    #     count = 0
    #     while sum1 <= dividend:
    #         sum1 += divisor
    #         count += 1
    #
    #     if -count < -2147483648:
    #         return -2147483648
    #     return -(count - 1)
    # elif divisor > 0 and dividend <0:
    #     dividend = dividend * -1
    #     print(divisor)
    #     sum1 = 0
    #     count = 0
    #     while sum1 <= dividend:
    #         sum1 += divisor
    #         count += 1
    #
    #     if -count < -2147483648:
    #         return -2147483648
    #     return -(count - 1)
    # else:
    #     if divisor<0 and dividend<0:
    #         dividend = dividend*-1
    #         divisor = divisor*-1
    #
    #     print(divisor)
    #     sum1 = 0
    #     count = 0
    #     while sum1 <= dividend:
    #         sum1 += divisor
    #         count += 1
    #
    #     if count > 2147483647:
    #         return 2147483647
    #     return count - 1
    a = abs(dividend)
    b = abs(divisor)

    negative = (dividend < 0 and divisor >= 0) or (dividend >= 0 and divisor < 0)

    output = 0

    while a >= b:
        counter = 1
        decrement = b

        while a >= decrement:
            a -= decrement

            output += counter
            counter += counter
            decrement += decrement

    output = output if not negative else -output

    return min(max(-2147483648, output), 2147483647)

print(divideTwoIntegers(-2147483648,-1))
