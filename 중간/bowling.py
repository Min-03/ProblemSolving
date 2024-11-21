def bowling(nums: list[int]) -> int:
    if not nums:
        return 0
    n = len(nums)
    dp = [0] * (n + 1)
    dp[0] = max(0, nums[0])
    for i in range(1, n):
        dp[i] = max(dp[i - 1], dp[i - 1] + nums[i], dp[i - 2] + nums[i] * nums[i - 1])
    
    # ret = []
    # curr = n - 1
    # while curr > 0:
    #     if dp[curr] == dp[curr - 1]:
    #         curr -= 1
    #     elif dp[curr] == dp[curr - 1] + nums[curr]:
    #         ret.append(curr)
    #         curr -= 1
    #     else:
    #         ret.append(curr)
    #         ret.append(curr - 1)
    #         curr -= 2
    # if curr == 0 and nums[0] > 0:
    #     ret.append(curr)
    # print(ret[::-1])
    return dp[n - 1]

def bowling(nums):
    n = len(nums)
    if n == 0:
        return 0
    oldPrev = 0
    prev = max(0, nums[0])
    for i in range(1, n):
        curr = max(prev, prev + nums[i], oldPrev + nums[i] * nums[i - 1])
        oldPrev = prev
        prev = curr
    return prev

# def bowling(nums: list[int]) -> int:
#     if not nums:
#         return 0
#     n = len(nums)

#     dp = [[0 for _ in range(3)] for _ in range(n + 1)]
#     dp[0][1] = nums[0]
#     for i in range(2, n):
#         dp[i][0] = max(dp[i - 1][0], dp[i - 1][1], dp[i - 1][2])
#         dp[i][1] = dp[i - 1][0] + nums[i]
#         dp[i][2] = dp[i - 2][0] + nums[i] * nums[i - 1]
#         print(dp[i][0], dp[i][1], dp[i][2])
#     return max(dp[n - 1][0], dp[n - 1][1], dp[n - 1][2])

if __name__ == "__main__":
    # nums = [-1, 1, 1, 1, 9, 9, 3, -3, -5, 2, 2]
    nums = [1]
    out = bowling(nums)
    print(out)
