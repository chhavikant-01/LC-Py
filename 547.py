class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        n = len(isConnected)
        visited = set()
        provinces = 0
        
        def dfs(city):
            # Visit each city that's connected to the current city
            for next_city in range(n):
                if isConnected[city][next_city] == 1 and next_city not in visited:
                    visited.add(next_city)
                    dfs(next_city)
        
        # Try to start DFS from each unvisited city
        for city in range(n):
            if city not in visited:
                visited.add(city)
                dfs(city)
                provinces += 1  # Found a new province
        
        return provinces
