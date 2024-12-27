class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        import heapq
    
        # Initialize two heaps: one for the first 'candidates' workers
        # and one for the last 'candidates' workers
        # Each element is (cost, index) to handle tie-breaking
        front_heap = []
        back_heap = []
        
        # Pointers to track which workers we've considered
        next_front = 0
        next_back = len(costs) - 1
        total_cost = 0
        
        # Initialize the heaps with the first and last 'candidates' workers
        # We'll add workers to front_heap from the start and back_heap from the end
        while len(front_heap) < candidates and next_front <= next_back:
            heapq.heappush(front_heap, (costs[next_front], next_front))
            next_front += 1
        
        while len(back_heap) < candidates and next_back >= next_front:
            heapq.heappush(back_heap, (costs[next_back], next_back))
            next_back -= 1
        
        # Process k hiring sessions
        for _ in range(k):
            # If we have no workers in the back heap, we must pick from front
            if not back_heap:
                cost, index = heapq.heappop(front_heap)
                total_cost += cost
                
                # Add next worker to front_heap if available
                if next_front <= next_back:
                    heapq.heappush(front_heap, (costs[next_front], next_front))
                    next_front += 1
                continue
                
            # If we have no workers in the front heap, we must pick from back
            if not front_heap:
                cost, index = heapq.heappop(back_heap)
                total_cost += cost
                
                # Add next worker to back_heap if available
                if next_back >= next_front:
                    heapq.heappush(back_heap, (costs[next_back], next_back))
                    next_back -= 1
                continue
            
            # Compare the minimum costs from both heaps
            # Remember: heap elements are (cost, index) tuples
            front_cost, front_index = front_heap[0]
            back_cost, back_index = back_heap[0]
            
            # Choose worker with lower cost, or lower index if costs are equal
            if front_cost <= back_cost:
                total_cost += heapq.heappop(front_heap)[0]
                if next_front <= next_back:
                    heapq.heappush(front_heap, (costs[next_front], next_front))
                    next_front += 1
            else:
                total_cost += heapq.heappop(back_heap)[0]
                if next_back >= next_front:
                    heapq.heappush(back_heap, (costs[next_back], next_back))
                    next_back -= 1
        
        return total_cost
        
