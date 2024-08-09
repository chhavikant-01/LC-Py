class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        self.n = len(nums)
        if self.n<3:
            return False
        self.a = 2**31 - 1
        self.b = 2**31 - 1 
        for i in range(self.n):
            if nums[i]<=self.a:
                self.a = nums[i]
            elif nums[i]<=self.b:
                self.b = nums[i]
            else: 
                return True
        
        return False
            
                
        