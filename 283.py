class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return None
        left = 0
        right = 0
        size = len(nums)
        
        while left<size and nums[left] != 0:
            left += 1
            right += 1
        # print(f"left ={left}  right={right}")

        while left<=right and right<size:
            # print(f"Running...")
            # print(f"left={nums[left]} at {left} index, right={nums[right]} at {right} index")
            if nums[left] == 0 and nums[right] != 0:
                #print(f"left={nums[left]}, right={nums[right]}")
                nums[left], nums[right] = nums[right], nums[left]
            while right < size and nums[right] == 0 :
                right += 1
            while left <= right and nums[left] != 0:
                left += 1

            


        
