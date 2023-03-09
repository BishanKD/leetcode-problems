def chalkReplacer(chalk, k):
        a = k % sum(chalk)
        for i in range(len(chalk)):
            a -= chalk[i]
            if(a<0):
                return i
            
chalk = [5,1,5]
k = 22
print(chalkReplacer(chalk, k))