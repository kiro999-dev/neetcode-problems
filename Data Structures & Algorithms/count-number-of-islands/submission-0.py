from collections import deque
from typing import List

class Solution:

    def __init__(self):
        self.visited = set()
    def isValid(self, row, col, nr, nc, grid):
        return (
            0 <= row < nr and
            0 <= col < nc and
            grid[row][col] == "1"
        )

    def nibr(self, row, col, grid):
        indicis = [
            (row + 1, col),
            (row - 1, col),
            (row, col + 1),
            (row, col - 1)
        ]

        return [
            (r, c)
            for r, c in indicis
            if self.isValid(r, c, len(grid), len(grid[0]), grid)
        ]
    def bfs(self,grid,row,col):
        q = deque()
        q.append((row, col))
        self.visited.add((row, col))

        while q:
            row, col = q.popleft()
            for nr, nc in self.nibr(row, col, grid):
                if (nr, nc) not in self.visited:
                    self.visited.add((nr, nc))
                    q.append((nr, nc))

    def numIslands(self, grid: List[List[str]]) -> int:
        counter = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1" and (row, col) not in self.visited:
                    self.bfs(grid,row,col)
                    counter+=1
        return counter