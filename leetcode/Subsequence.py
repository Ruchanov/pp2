def maxCoins(nums):
    coins = 0
    while len(nums) != 0:
        if len(nums)>3:
            c = 1
            for i in range(3):
                c *= nums[i]
            print(c)
            coins += c
            nums.pop(nums.index(min(nums)))
        else:
            c = 1
            for i in range(len(nums)):
                c *= nums[i]
            print(c)
            coins += c
            nums.pop(nums.index(min(nums)))
    return coins
print(maxCoins([3,1,5,8]))