class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:


        if len(nums) == 1:
            if nums[0] == k: return 1
            else: return 0
        nums.sort()

        left = 0 
        right = len(nums) - 1
        operation = 0 

        while left < right:
            if ((nums[left] + nums[right]) == k):
                operation += 1
                left +=1 
                right -=1
            elif((nums[left] + nums[right]) < k):
                left += 1
            else:
                right -= 1
        return operation
