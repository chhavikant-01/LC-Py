from heapq import heappush, heappop

class SmallestInfiniteSet:
    def __init__(self):
        # This represents the smallest number in our infinite sequence
        # Initially, it's 1 since we start with all positive integers
        self.current_min = 1
        
        # Min-heap to store numbers that were added back
        # Only numbers smaller than current_min need to be stored
        self.added_numbers = []
        
        # Set to check for duplicates efficiently
        # Contains same numbers as the heap
        self.added_set = set()

    def popSmallest(self):
        # If we have numbers that were added back
        if self.added_numbers:
            # Get the smallest number from our heap
            smallest = heappop(self.added_numbers)
            # Remove it from our set as well
            self.added_set.remove(smallest)
            return smallest
        else:
            # If no added-back numbers, return and increment current_min
            smallest = self.current_min
            self.current_min += 1
            return smallest

    def addBack(self, num):
        # Only add the number if:
        # 1. It's smaller than current_min (meaning it was previously removed)
        # 2. It's not already in our added numbers set
        if num < self.current_min and num not in self.added_set:
            heappush(self.added_numbers, num)
            self.added_set.add(num)
