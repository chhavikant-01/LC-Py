class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        # Get maze dimensions
        rows, cols = len(maze), len(maze[0])
        
        # Define the four possible directions: up, right, down, left
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        
        # Create a queue for BFS: (row, col, steps)
        queue = deque([(entrance[0], entrance[1], 0)])
        
        # Mark entrance as visited to avoid going back
        maze[entrance[0]][entrance[1]] = '+'
        
        def is_exit(row: int, col: int) -> bool:
            """
            Check if the current cell is an exit:
            1. Must be at the border
            2. Must not be the entrance
            3. Must be an empty cell ('.')
            """
            is_border = row == 0 or row == rows - 1 or col == 0 or col == cols - 1
            is_entrance = [row, col] == entrance
            return is_border and not is_entrance
        
        # Start BFS
        while queue:
            row, col, steps = queue.popleft()
            
            # Check all four directions
            for dx, dy in directions:
                new_row, new_col = row + dx, col + dy
                
                # Check if the new position is valid and unvisited
                if (0 <= new_row < rows and 
                    0 <= new_col < cols and 
                    maze[new_row][new_col] == '.'):
                    
                    # If we found an exit, return the number of steps
                    if is_exit(new_row, new_col):
                        return steps + 1
                    
                    # Mark as visited and add to queue
                    maze[new_row][new_col] = '+'
                    queue.append((new_row, new_col, steps + 1))
        
        # If we haven't found an exit, return -1
        return -1
        
