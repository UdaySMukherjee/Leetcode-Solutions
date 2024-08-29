class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)  # Total number of stones
        visited = [False] * n  # To track if a stone has been visited during DFS
        rows = defaultdict(list)  # Dictionary to map rows to stone indices
        cols = defaultdict(list)  # Dictionary to map columns to stone indices
        ans = 0  # Initialize the number of stones that can be removed

        # Populate rows and cols dictionaries
        for i, point in enumerate(stones):
            rows[point[0]].append(i)  # Map row index to stone index
            cols[point[1]].append(i)  # Map column index to stone index

        # Depth-first search to explore all connected stones
        def dfs(node):
            visited[node] = True  # Mark the current stone as visited
            count = 1  # Initialize count of connected stones

            # Traverse all stones in the same row
            for x in rows[stones[node][0]]:
                if not visited[x]:
                    count += dfs(x)  # Recursively perform DFS on unvisited stones in the same row

            # Traverse all stones in the same column
            for x in cols[stones[node][1]]:
                if not visited[x]:
                    count += dfs(x)  # Recursively perform DFS on unvisited stones in the same column

            return count  # Return the total number of connected stones

        # Iterate through all stones to perform DFS from each unvisited stone
        for i in range(n):
            if not visited[i]:
                size = dfs(i)  # Find the size of the connected component
                ans += size - 1  # Add the number of stones that can be removed in this component

        return ans  # Return the total number of stones that can be removed
