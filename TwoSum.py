def twoSum(nums, target):
    for i in range(len(nums)):
            a = nums[i]
            b = target - a
            nums[i]= float('inf')
            if b in nums:
                return [i, nums.index(b)]
            
nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))
        



