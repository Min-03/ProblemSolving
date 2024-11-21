# def knapsack(values, weights, limit):
#     dp = [0] * (limit + 1)
#     for v, w in zip(values, weights):
#         for i in reversed(range(w, limit + 1)):
#             dp[i] = max(dp[i], dp[i - w] + v)
#     return dp[limit]

def knapsack(costs, values, least):
    maxVal = sum(values)
    dp = [float("inf")] * (maxVal + 1) #minimum cost for getting exact i val
    dp[0] = 0
    for cost, value in zip(costs, values):
        for i in reversed(range(value, maxVal + 1)):
            dp[i] = min(dp[i], dp[i - value] + cost)
    return dp[least]

def power_set(A):
    sets = [[]]
    for n in A:
        newSets = []
        for curr in sets:
            new = curr.copy()
            new.append(n)
            newSets.append(new)
        sets.extend(newSets)
    return sets

def permute(s: str) -> list[str]:
    ans = []
    _permute(list(s), 0, ans)
    return ans

def _permute(s, idx, ans):
    if idx == len(s):
        ans.append("".join(s))
        return
    for i in range(idx, len(s)):
        s[i], s[idx] = s[idx], s[i]
        _permute(s, idx + 1, ans)
        s[i], s[idx] = s[idx], s[i]



# weights = [6, 4, 3, 5]
# values = [13, 8, 6, 12]
values = [1, 1, 1, 5, 13, 3]
costs = [1, 1, 1, 5, 10, 12]
# print(knapsack(costs, values, 15))
A = [1, 2, 4]
print(permute("abc"))