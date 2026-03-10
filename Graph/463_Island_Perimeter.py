# ------------------------------------------------------------
# Problem: Island Perimeter
#
# Approach: DFS (Depth First Search)
#
# Idea:
# The perimeter of the island increases whenever a land cell
# touches water or the boundary of the grid.
#
# Steps:
#
# 1. Get number of rows and columns in the grid.
#
# 2. Use a set called "visit" to store visited land cells
#    to avoid visiting the same cell again.
#
# 3. Define a DFS function dfs(i, j):
#
#    Base Case:
#    - If the cell goes outside the grid -> return 1
#    - If the cell is water (grid[i][j] == 0) -> return 1
#      because that edge contributes to the perimeter.
#
#    If the cell is already visited:
#    - return 0 to avoid double counting.
#
#    Otherwise:
#    - Mark the cell as visited.
#
#    - Recursively explore all 4 directions:
#        right  -> dfs(i, j + 1)
#        down   -> dfs(i + 1, j)
#        left   -> dfs(i, j - 1)
#        up     -> dfs(i - 1, j)
#
#    - Add the results of all four DFS calls.
#
# 4. Traverse the grid to find the first land cell (value = 1).
#
# 5. Start DFS from that land cell and return the result.
#
# 6. DFS will explore the whole island and count every edge
#    that touches water or boundary, which forms the perimeter.
#
# Time Complexity:  O(rows * cols)
# Space Complexity: O(rows * cols) (visited set + recursion stack)
#
# ------------------------------------------------------------


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()

        def dfs(i, j):
            if i < 0 or j < 0 or i >= rows or j >= cols or grid[i][j] == 0:
                return 1
            if (i, j) in visit:
                return 0

            visit.add((i, j))
            perim = dfs(i, j + 1) + dfs(i + 1, j) + dfs(i, j - 1) + dfs(i - 1, j)
            return perim

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]:
                    return dfs(i, j)
        return 0