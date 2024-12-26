class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        fresh_count = 0
        rotten = deque()
        
        # Find all rotten oranges and count fresh oranges
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    rotten.append((i, j))
                elif grid[i][j] == 1:
                    fresh_count += 1
        
        # If no fresh oranges, return 0
        if fresh_count == 0:
            return 0
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        minutes = 0
        
        # BFS starting from all rotten oranges
        while rotten and fresh_count > 0:
            minutes += 1
            
            # Process all oranges that became rotten at the same time
            for _ in range(len(rotten)):
                x, y = rotten.popleft()
                
                # Check all 4 adjacent cells
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    
                    # If in bounds and is fresh orange
                    if (0 <= nx < rows and 0 <= ny < cols and 
                        grid[nx][ny] == 1):
                        grid[nx][ny] = 2  # Make it rotten
                        fresh_count -= 1
                        rotten.append((nx, ny))
        
        # If there are still fresh oranges, impossible to rot all
        return minutes if fresh_count == 0 else -1
        
