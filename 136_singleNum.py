def singleNum(nums):
        nums.sort()
        if(len(nums)==1):
            return nums[0]
        else:
            if(nums[0]==nums[1]):
                pass
            else:
                return nums[0]    
            for i in range(2,len(nums)-1):
                if(nums[i]==nums[i+1] or nums[i]==nums[i-1]):
                    continue
                else:
                    return nums[i]
                    break
            if(nums[len(nums)-1]!=nums[len(nums)-2]):
                return nums[len(nums)-1]