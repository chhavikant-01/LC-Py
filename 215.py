class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Create a min heap
        heap = []
        
        # Process each number
        for num in nums:
            # Add number to heap
            heapq.heappush(heap, num)
            # If heap size exceeds k, remove smallest element
            if len(heap) > k:
                heapq.heappop(heap)
        
        # The root of heap will be kth largest element
        return heap[0]
