def climbingStairs(n):
    if n == 1:
        return n
    step1 = 1
    step2 = 2
    for i in range(3, n+1):
        current_step = step1 + step2
        step1 = step2
        step2 = current_step
    return step2
print(climbingStairs(5))