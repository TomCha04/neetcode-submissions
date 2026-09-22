class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # element on coordinate (x,y) = element on grid[row][col]
        # 1) iterate over the grid
        # 2) once we hit a 1, two things happen:
        # 2.1) increase count by 1.
        # 2.2) recursively run DFS on that 1 to find other 1s
        # 3) repeat steps 1 through 2.2
        count = 0

        def dfs(row, col):
            # return immediately if neighbor is out of bounds or is 0
            if 0 <= row < len(grid) and 0 <= col < len(grid[row]) and grid[row][col] == "1":
                grid[row][col] = "0" # turn visited 1s into 0s
                dfs(row, col+1) # explore right neighbor
                dfs(row, col-1) # explore left neighbor
                dfs(row+1, col) # explore top neighbor
                dfs(row-1, col) # explore bottom neighbor
                return
            else: return 

        # row and col are NUMBERS, not the actual lists
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == "1":
                    count += 1 
                    dfs(row, col)
        return count