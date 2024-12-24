class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # Step 1: Build the graph
        # We'll create an adjacency list where each node maps to a list of (neighbor, value) pairs
        # For a/b = 2, we'll add two edges: a->b (2) and b->a (1/2)
        graph = {}
        
        def add_edge(x, y, val):
            if x not in graph:
                graph[x] = []
            if y not in graph:
                graph[y] = []
            # Add both forward and reverse edges
            graph[x].append((y, val))
            graph[y].append((x, 1/val))
        
        # Build the graph from equations
        for (x, y), val in zip(equations, values):
            add_edge(x, y, val)
        
        def find_path(start: str, end: str, visited: set) -> float:
            """
            Uses DFS to find the result of division from start to end variables.
            Returns -1.0 if no path exists.
            """
            # Base cases
            if start not in graph or end not in graph:
                return -1.0
            if start == end:
                return 1.0
                
            visited.add(start)
            
            # Try all possible paths from current node
            for neighbor, value in graph[start]:
                if neighbor not in visited:
                    # Recursively find path to target
                    # The result will be current edge value * rest of the path
                    sub_path = find_path(neighbor, end, visited)
                    if sub_path != -1.0:
                        return value * sub_path
            
            visited.remove(start)
            return -1.0
        
        # Process each query using DFS
        results = []
        for start, end in queries:
            results.append(find_path(start, end, set()))
            
        return results
