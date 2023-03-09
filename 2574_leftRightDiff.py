def leftRightDifference(nums):
        answer = [sum(nums)-nums[0]]
        leftSum = [0]
        rightSum = [sum(nums)-nums[0]]
        for i in range(1,len(nums)):
            leftSum.append(leftSum[i-1]+nums[i-1])
            rightSum.append(rightSum[i-1]-nums[i])
            if(leftSum[i]>rightSum[i]):
                answer.append(leftSum[i]- rightSum[i])
            else:
                answer.append(rightSum[i]-leftSum[i])
        return answer

nums = [2,3,-1,8,4]
print(leftRightDifference(nums))