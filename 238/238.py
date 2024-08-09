class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        self.product_list = []
        for i in range(len(nums)):
            self.product_list.append(1)
        self.curr = 1
        for i in range(len(nums)):
            self.product_list[i] *= self.curr
            self.curr *=nums[i]
        
        self.curr = 1
        for i in range(len(nums)-1,-1,-1):
            self.product_list[i] *=self.curr
            self.curr *= nums[i]