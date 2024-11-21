import sys

def longest_zero_sum(arr: list[int]) -> int:
  # TODO
  hi = 0
  prefix_sum = {0:-1}
  ssum = 0
  for i, num in enumerate(arr):
    ssum += num
    if ssum in prefix_sum:
      hi = max(hi, i - prefix_sum[ssum])
    else:
      prefix_sum[ssum] = i
  return hi

def longest_k_sum(arr: list[int], k: int) -> int:
  prefix_sum = {0:-1}
  ssum = 0
  hi = 0
  for i, num in enumerate(arr):
    ssum += num
    if ssum - k in prefix_sum:
      hi = max(hi, i - prefix_sum[ssum - k])
    if ssum not in prefix_sum:
      prefix_sum[ssum] = i
  return hi

  
def test():
  arr = [15, -2, 2, -8, 1, 7, 10, 23]
  arr = [1, 0, 0, 0, 0, 2, -2, 3, 5]
  # input: [15, -2, 2, -8, 1, 7, 10, 23]
  # output: 5
  arr = [1, 2, 3, -3, -1, -2]
  arr = [1, 2, 3, 1, 2]
  n = longest_zero_sum(arr)
  print(n)
  print(longest_k_sum(arr, 5))


if __name__ == '__main__':
  test()
