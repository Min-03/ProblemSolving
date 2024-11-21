from collections import deque

def robot(grid: list[list[int]]) -> list[tuple]:
  if not grid or not grid[0] or grid[0][0]:
     return None
  r, c = len(grid), len(grid[0])
  visited = [[False for _ in range(c)] for _ in range(r)]
  before = [[(0, 0) for _ in range(c)] for _ in range(r)]
  q = deque([(0, 0)])
  visited[0][0] = True
  while q:
     x, y = q.popleft()
     if x == r - 1 and y == c - 1:
        break
     for nx, ny in ((x + 1, y), (x, y + 1)):
        if nx >= r or ny >= c or grid[nx][ny] or visited[nx][ny]:
           continue
        q.append((nx, ny))
        visited[nx][ny] = True
        before[nx][ny] = (x, y)
   #   if y + 1 < c and not grid[x][y + 1] and not visited[x][y + 1]:
   #      q.append((x, y + 1))
   #      visited[x][y + 1] = True
   #      before[x][y + 1] = (x, y)
   #   if x + 1 < r and not grid[x + 1][y] and not visited[x + 1][y]:
   #      q.append((x + 1, y))
   #      visited[x + 1][y] = True
   #      before[x + 1][y] = (x, y)

  if not visited[r - 1][c - 1]:
     return None 
  ret = []
  x, y = r - 1, c - 1
  while x != 0 or y != 0:
     ret.append((x, y))
     x, y = before[x][y]
  ret.append((0, 0))
  return ret[::-1]

# def get_path(G, xs, ys, xt, yt, path, is_failed):
#  r, c = len(G), len(G[0])
#  cands = [(xs+1, ys), (xs, ys+1)]
#  for xn, yn in cands:
#    if xn >= r or yn >= c \
#    or G[xn][yn] or (xn, yn) in is_failed:
#       continue
#    path.append((xn, yn))
#    if (xn, yn) == (xt, yt):
#       return path
#    else:
#       output = get_path(G, xn, yn, xt, yt, path, is_failed)
#       if not output: is_failed.add((xn, yn))
#       if output is not None: return output
#    path.pop()
#  is_failed.add((xs, ys))
#  return None 

# def robot(grid):
#  if not grid or not grid[0]:
#    return []
#  s = (0, 0)
#  t = (len(grid)-1, len(grid[0])-1)
#  if s == t:
#    return [s]
#  else:
#    is_failed = set()
#    return get_path(grid, *s, *t, [s], is_failed)


if __name__ == "__main__":
    # Example 1
    grid = [[0, 0, 1, 1],
            [1, 0, 0, 1],
            [0, 0, 1, 1],
            [0, 1, 1, 1],
            [0, 0, 0, 0]]
    print("Example 1:", grid)
    path = robot(grid)
    print("Path:", path)

    # Example 2
    grid = [[0, 0, 0, 1, 0],
            [0, 1, 0, 1, 0],
            [0, 1, 0, 1, 1],
            [0, 1, 0, 0, 0],
            [0, 0, 0, 1, 0]]
    print("Example 2:", grid)
    path = robot(grid)
    print("Path:", path)

