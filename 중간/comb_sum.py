from typing import List

# def backtrack(candidates, target, used, idx, ans):
#    if idx == len(candidates):
#       res = []
#       ssum = 0
#       for i in range(len(candidates)):
#          if used[i]:
#             res.append(candidates[i])
#             ssum += candidates[i]
#       if ssum == target:
#          ans.add(tuple(res))
#       return
#    used[idx] = True
#    backtrack(candidates, target, used, idx + 1, ans)
#    used[idx] = False
#    backtrack(candidates, target, used, idx + 1, ans)
   

# def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
#   candidates = sorted(candidates)
#   ans = set()
#   used = [False] * len(candidates)
#   backtrack(candidates, target, used, 0, ans)
#   ans = list(ans)
#   ans = list(map(list, ans))
#   return ans

def combination_sum(candidates, target):
    ans = []
    candidates.sort()
    backtrack(candidates, 0, target, [], ans)
    return ans

def backtrack(nums, idx, target, res, ans):
    for i in range(idx, len(nums)):
        if i > idx and nums[i] == nums[i - 1]:
            continue
        if nums[i] == target:
            res.append(nums[i])
            ans.append(res.copy())
            res.pop()
        elif nums[i] < target:
            res.append(nums[i])
            backtrack(nums, i + 1, target - nums[i], res, ans)
            res.pop()

if __name__ == '__main__':
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    ans = combination_sum(candidates, target)
    print("Example 1")
    print(f"candidates: {candidates}")
    print(f"target: {target}")
    print(f"ans: {ans}")
    print("*"*50)
    print("Example 2")
    candidates = [2, 5, 2, 1, 2]
    target = 5
    ans = combination_sum(candidates, target)
    print(f"candidates: {candidates}")
    print(f"target: {target}")
    print(f"ans: {ans}")
