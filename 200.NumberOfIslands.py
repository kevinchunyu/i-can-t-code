class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # clarify that i can do this because of constraints
        row_len = len(grid)
        col_len = len(grid[0])
        
        island_count = 0 
        for i in range(row_len):
            for j in range(col_len):
                if grid[i][j] == '1': 
                    self.dfs(grid, i, j)
                    island_count += 1


        return island_count

    def dfs(self, grid, row, col): 
        # if at border 
        if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] == '0':
            return

        grid[row][col] = '0'

        # consider four directions              
        self.dfs(grid, row + 1, col)
        self.dfs(grid, row - 1, col)
        self.dfs(grid, row, col + 1)
        self.dfs(grid, row, col - 1)