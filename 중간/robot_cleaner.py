# from collections import deque

# def robot(grid: list[list[int]], row:int, col:int):
#     listOfCandidates = []
#     n, m = len(grid), len(grid[0])
#     before = [[(0, 0) for _ in range(m)] for _ in range(n)]
#     visited = [[False for _ in range(m)] for _ in range(n)]
#     dx = [1, -1, 0, 0]
#     dy = [0, 0, 1, -1]
#     q = deque()
#     q.append((row, col))
#     while q:
#         x, y = q.popleft()
#         if x == n - 1 and y == m - 1:
#             break
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if (0 <= nx and nx < n and 0 <= ny and ny < m and grid[nx][ny] != 1 and not visited[nx][ny]):
#                 visited[nx][ny] = True
#                 before[nx][ny] = (x, y)
#                 q.append((nx, ny))
#     if not visited[n - 1][m - 1]:
#         return None
#     x, y = n - 1, m - 1
#     while x != row or y != col:
#         listOfCandidates.append((x, y))
#         x, y = before[x][y]
#     listOfCandidates.append((x, y))
#     return listOfCandidates[::-1]

def robot(grid: list[list[int]], row: int, col: int):
    def dfs(grid, row, col):
        grid[row][col] = 2
        for (i, j) in [(0, 1), (-1, 0), (0, -1), (1, 0)]:
            x, y = (row + i, col + j)
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 0:
                dfs(grid, x, y)
    dfs(grid, row, col)

    # visited = set()
    # def dfs(grid, row, col, visited):
    #     visited.add((row, col))
    #     for (i, j) in [(0, 1), (-1, 0), (0, -1), (1, 0)]:
    #         x, y = (row + i, col + j)
    #         if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 0 and (x, y) not in visited:
    #             dfs(grid, x, y, visited)
    # dfs(grid, row, col, visited)


if __name__ == "__main__":
    # Example 1
    grid = [[0, 0, 1, 1],
            [1, 0, 0, 1],
            [0, 0, 1, 1],
            [0, 1, 1, 1],
            [0, 0, 0, 0]]
    print("Example 1:", grid)
    path = robot(grid, 0, 0)
    print("Path:", path)

    # Example 2
    grid = [[0, 0, 1, 1],
            [1, 0, 1, 1],
            [0, 0, 0, 0],
            [0, 1, 1, 0],
            [0, 0, 0, 0]]
    print("Example 2:", grid)
    path = robot(grid, 0, 0)
    print("Path:", path)