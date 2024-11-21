import os

ret = []

def get_grid_cost(cost: list[list[int]]) ->int:
    n = len(cost)
    m = len(cost[0])
    dp = [[0 for _ in range(m)] for _ in range(n)]
    for j in range(m):
        dp[n - 1][j] = cost[n - 1][j]
    for i in range(n - 2, -1, -1):
        for j in range(m):
            dp[i][j] = dp[i + 1][j]
            if j > 0 and dp[i][j] > dp[i + 1][j - 1]:
                dp[i][j] = dp[i + 1][j - 1]
            if j < m - 1 and dp[i][j] > dp[i + 1][j + 1]:
                dp[i][j] = dp[i + 1][j + 1]
            dp[i][j] += cost[i][j]
    lo = 1e9
    for j in range(m):
        lo = min(lo, dp[0][j])
    return lo

# def get_lcs_len(x, y, dp):
#     n, m = len(x), len(y)
#     for i in range(1, n):
#         for j in range(1, m):
#             dp[i][j] = dp[i - 1][j - 1] + 1 if x[i] == y[j] \
#                 else max(dp[i - 1][j], dp[i][j - 1])
#     return dp[n - 1][m - 1]

# def print_lcs(x, y, dp, idx1, idx2, curr_len, lcs_len, res, ans):
#     if curr_len == lcs_len:
#         ans.append("".join(reversed(res)))
#         return
#     found = set()
#     for i in reversed(range(0, idx1 + 1)):
#         if x[i] in found:
#             continue
#         for j in reversed(range(0, idx2 + 1)):
#             if x[i] == y[j] and lcs_len - curr_len == dp[i][j]:
#                 res[curr_len] = x[i]
#                 found.add(x[i])
#                 print_lcs(x, y, dp, i - 1, j - 1, curr_len + 1, lcs_len, res, ans)
#                 break

# def longest_common_subsequence(x, y):
#     x = ' ' + x
#     y = ' ' + y
#     dp = [[0 for _ in range(len(y))] for _ in range(len(x))]
#     ans = []
#     lcs_len = get_lcs_len(x, y, dp)
#     print_lcs(x, y, dp, len(x) - 1, len(y) - 1, 0, lcs_len, ['_'] * lcs_len, ans)
#     return ans

def print_lcs(x, y, idx1, idx2, curr_len, lcs_len, dp, res, ans):
    if curr_len == lcs_len:
        ans.append("".join(reversed(res)))
        return
    found = set()
    for i in reversed(range(0, idx1 + 1)):
        if x[i] in found:
            continue
        for j in reversed(range(0, idx2 + 1)):
            if x[i] == y[j] and lcs_len - curr_len == dp[i][j]:
                res[curr_len] = x[i]
                found.add(x[i])
                print_lcs(x, y, i - 1, j - 1, curr_len + 1, lcs_len, dp, res, ans)
                break


def longest_common_subsequence(x, y):
    if not x or not y:
        return []
    x = ' ' + x
    y = ' ' + y
    n, m = len(x), len(y)
    dp = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = dp[i - 1][j - 1] + 1 if x[i] == y[j] else \
                max(dp[i - 1][j], dp[i][j - 1])
    ans = []
    print_lcs(x, y, len(x) - 1, len(y) - 1, 0, dp[n - 1][m - 1], dp, ['_'] * dp[n - 1][m - 1], ans)
    return ans

if __name__ == "__main__":
    x = "HIEROGLYPHOLOGY"
    y = "MICHAELANGELO"
    # x = "ABCBDAB"
    # y = "BDCABA"
    ret = longest_common_subsequence(x, y)
    print(ret)
    # cost = [[2, 8, 9, 5, 8],
    #         [4, 4, 6, 2, 3],
    #         [5, 7, 5, 6, 1],
    #         [3, 2, 5, 4, 8]]
    # print(get_grid_cost(cost))
    
