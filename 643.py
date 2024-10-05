class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if k>len(nums):
            return
        currentSum = 0
        for i in range(0,k):
            currentSum+=nums[i]
        
        maxx = currentSum
        for i in range(k,len(nums)):
            currentSum = currentSum - nums[i-k] + nums[i]
            if(currentSum > maxx):
                maxx = currentSum

        return maxx/k
