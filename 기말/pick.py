import random

def pick(nums, target):
  cnt = 0
  ret = -1
  for i, num in enumerate(nums):
    if num != target:
      continue
    if random.randint(1, cnt + 1) == 1:
      ret = i
    cnt += 1
  return ret

if __name__ == '__main__':
  nums = [1,2,3,3,3]
  target = 3
  output = pick(nums, target)
  print(output) # The output for the above example is 0.