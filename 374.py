# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        # Initialize our search range
        left = 1       # The smallest possible number
        right = n      # The largest possible number
        
        # Continue searching while we have a valid range
        while left <= right:
            # Calculate the middle point, avoiding potential integer overflow
            # Instead of (left + right) // 2, we use this safer formula:
            mid = left + (right - left) // 2
            
            # Make a guess and get the response
            result = guess(mid)
            
            # If we found the number, return it
            if result == 0:
                return mid
            
            # If our guess was too high, look in the lower half
            elif result == -1:
                right = mid - 1
            
            # If our guess was too low, look in the upper half
            else:  # result == 1
                left = mid + 1

        # This line should never be reached given the problem constraints
        return -1
