class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        i, j = 0, 0
        h = len(grid) - 1
        w = len(grid[0]) - 1
        visited = set()
        count = 0

        for x in range(len(grid)):
            for y in range(len(grid[0])):

                if (x, y) in visited or grid[x][y] == "0":
                    continue

                island = [[x, y]]

                while island:
                    i, j = island.pop()
                    visited.add((i, j))

                    if i > 0:
                        if grid[i-1][j] == "1" and (i-1,j) not in visited:
                            island.append([i-1, j])
                    if i < h:
                        if grid[i+1][j] == "1" and (i+1,j) not in visited:
                            island.append([i+1, j])
                    if j > 0:
                        if grid[i][j-1] == "1" and (i,j-1) not in visited:
                            island.append([i, j-1])
                    if j < w:
                        if grid[i][j+1] == "1" and (i,j+1) not in visited:
                            island.append([i, j+1])

                count += 1

        return count


        