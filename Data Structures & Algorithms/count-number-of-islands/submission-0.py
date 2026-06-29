class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        grid = [
            ["0","0","0","0","1"],
            ["0","0","0","0","1"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]
        ]

        keep track of all neighbor 1s and visit them - to count each island, and visit it completely.
        
        But where to start off from next once an island is completely visited?

        Save all 1s to a list initially to mark unvisited points, and start from there.
        """
        num_rows, num_cols = len(grid), len(grid[0])

        def dfs(row, col):
            grid[row][col] = "0"

            if row+1 < num_rows and grid[row+1][col] == "1":
                dfs(row+1, col)
            if col+1 < num_cols and grid[row][col+1] == "1":
                dfs(row, col+1)
            if row-1 >= 0 and grid[row-1][col] == "1":
                dfs(row-1, col) 
            if col-1 >= 0 and grid[row][col-1] == "1":
                dfs(row, col-1)

        counter = 0
        
        for row in range(num_rows):
            for col in range(num_cols):
                # island
                if grid[row][col] == "1":
                    # dfs complete island and mark visited
                    # update counter += 1
                    dfs(row, col)
                    counter += 1
        
        return counter