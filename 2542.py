class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # First, create pairs of (nums2[i], nums1[i]) and sort by nums2 in descending order
        # We sort by nums2 descending because we want to try larger minimum values first
        pairs = sorted(zip(nums2, nums1), reverse=True)
        
        # Use a min heap to maintain the k-1 largest values from nums1 
        # that we've seen so far
        import heapq
        n1sum = 0  # Keep track of the sum of selected nums1 values
        heap = []  # Min heap to store selected nums1 values
        
        # Initialize the maximum score
        max_score = 0
        
        # For each index i, consider using pairs[i][0] as the minimum value from nums2
        for n2, n1 in pairs:
            heapq.heappush(heap, n1)
            n1sum += n1
            
            # If we have more than k elements, remove the smallest one
            if len(heap) > k:
                n1sum -= heapq.heappop(heap)
            
            # If we have exactly k elements, calculate the score
            if len(heap) == k:
                score = n1sum * n2  # n2 is the minimum value from nums2
                max_score = max(max_score, score)
        
        return max_score
        
