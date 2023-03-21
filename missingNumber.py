def miss(nums):
    n = len(nums)
    for i in range(n + 1):
        if i not in nums:
            return i
    return n + 1

print(miss([3,0,1]))