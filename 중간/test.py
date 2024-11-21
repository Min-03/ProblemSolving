def get_edit_distance(x, y):
  if not x or not y:
    return len(x) + len(y)
  x, y = ' ' + x, ' ' + y
  n, m = len(x), len(y)
  dp = [[1e9 for _ in range(m)] for _ in range(n)]
  for i in range(n):
    dp[i][0] = i
  for j in range(m):
    dp[0][j] = j

  for i in range(1, n):
    for j in range(1, m):
      if x[i] == y[j]:
        dp[i][j] = dp[i - 1][j - 1]
      else:
        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

  return dp[n - 1][m - 1]



# x = input()
# y = input()
# dist = get_edit_distance(x, y)
# print(dist)
def house_robber(nums):
    n = len(nums)
    dp = [0] * n
    prev = [0] * n
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    prev[0] = -2
    prev[1] = -1 if nums[1] > nums[0] else 0
    for i in range(2, n):
        if dp[i - 2] + nums[i] > dp[i - 1]:
            dp[i] = dp[i - 2] + nums[i]
            prev[i] = i - 2
        else:
            dp[i] = dp[i - 1]
            prev[i] = i - 1

    ret = []
    curr = n - 1
    while (curr >= 0):
        if prev[curr] == curr - 2:
            ret.append(nums[curr])
        curr = prev[curr]
    print(ret[::-1])
    return dp[n - 1]


def print_lcs(x, y, i, j, dp, ans):
    if i == 0 or j == 0:
        return
    if x[i] == y[j]:
        print_lcs(x, y, i - 1, j - 1, dp, ans)
        ans.append(x[i])
    elif dp[i - 1][j] > dp[i][j - 1]:
        print_lcs(x, y, i - 1, j, dp, ans)
    else:
        print_lcs(x, y, i, j - 1, dp, ans)

def lcs(x, y):
    x, y = ' ' + x, ' ' + y
    n, m = len(x), len(y)
    dp = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(1, n):
        for j in range(1, m):
            if x[i] == y[j]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    print(dp[n - 1][m - 1])
    ans = []
    print_lcs(x, y, n - 1, m - 1, dp, ans)
    print("".join(ans))

# def get_grid(grid):
#     n, m = len(grid), len(grid[0])
#     dp = [[0 for _ in range(m)] for _ in range(n)]
#     for j in range(m):
#         dp[0][j] = grid[0][j]
#     for i in range(1, n):
#         for j in range(m):
#             dp[i][j] = dp[i - 1][j]
#             if j > 0 and dp[i][j] > dp[i - 1][j - 1]:
#                 dp[i][j] = dp[i - 1][j - 1]
#             if j < m - 1 and dp[i][j] > dp[i - 1][j + 1]:
#                 dp[i][j] = dp[i - 1][j + 1]
#             dp[i][j] += grid[i][j]
#     lo = float("inf")
#     for j in range(m):
#         lo = min(lo, dp[n - 1][j])
#     return lo

def get_grid(grid):
   n, m = len(grid), len(grid[0])
   dp = [[0 for _ in range(m + 1)] for _ in range(n)]
   for j in range(m):
      dp[0][j] = grid[0][j]
   for i in range(n):
      dp[i][m] = float("inf")
   for i in range(1, n):
      for j in range(m):
         dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i - 1][j + 1]) + grid[i][j]
   lo, lo_idx = float("inf"), -1
   for j in range(m):
      if lo > dp[n - 1][j]:
         lo = dp[n - 1][j]
         lo_idx = j
   print_opt(n - 1, lo_idx, dp, grid)
   return lo

def print_opt(i, j, dp, grid):
   if i == 0:
      print(i, j)
      return
   elif dp[i][j] == dp[i - 1][j - 1] + grid[i][j]:
      print_opt(i - 1, j - 1, dp, grid)
   elif dp[i][j] == dp[i - 1][j] + grid[i][j]:
      print_opt(i - 1, j, dp, grid)
   else:
      print_opt(i - 1, j + 1, dp, grid)
   print(i, j)

if __name__ == "__main__":
    nums = [3, 7, 8, 2, 1]
    # print(house_robber(nums))
    x = "HIEROGLYPHOLOGY"
    y = "MICHAELANGELO"
    # lcs(x, y)
    grid = [[2, 8, 9, 5, 8],
            [4, 4, 6, 2, 3],
            [5, 7, 5, 6, 1],
            [3, 2, 5, 4, 8]]
    # print(get_grid(grid))

    a = [1]
    for _ in range(len(a)):
       a.append(1)
       print(len(a))


