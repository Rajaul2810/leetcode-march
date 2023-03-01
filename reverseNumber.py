def reverses(x):

            if x<0:
                temp = x*-1
                rev = 0
                while temp>0:
                    dig = temp%10
                    rev = rev*10+dig
                    temp = temp//10
                if rev < -2147483648 or rev > 2147483647:
                    return 0
                return -rev
            else:
                rev = 0
                while x>0:
                    dig = x%10
                    rev = rev*10+dig
                    x = x//10
                if rev < -2147483648 or rev > 2147483647:
                    return 0
                return rev

print(reverses(1534236469))