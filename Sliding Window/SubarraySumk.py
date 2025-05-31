def subarraySum(self, nums: List[int], k: int) -> int:
    count=0
    for i in range(0,len(nums)):
        if nums[i]==k:
            count+=1
        j=i+1
            sumOfWin=nums[i]
            while j<=len(nums)-1:
                sumOfWin=sumOfWin+nums[j]                   
                if sumOfWin==k:
                    count+=1
                j+=1
        return count
