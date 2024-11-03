class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        res = []

        for a in asteroids:

            while res and a < 0 < res[-1]:  # While there is a possible collision
                if -a > res[-1]:  # The new asteroid destroys the last one
                    res.pop()
                    continue
                elif -a == res[-1]:  # Both asteroids destroy each other
                    res.pop()
                break  # If the last asteroid survives, break out of the while loop
            else:
                # This else is executed if the `while` loop didn't break (no collision or all previous asteroids destroyed)
                res.append(a)

        return res
