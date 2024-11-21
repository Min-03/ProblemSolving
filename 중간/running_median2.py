import heapq

def running_median(nums):
  ret = []
  lo = []
  hi = []
  for num in nums:
    heapq.heappush(lo, -num)
    heapq.heappush(hi, -heapq.heappop(lo))
    if len(lo) < len(hi):
      heapq.heappush(lo, -heapq.heappop(hi))
    median = -lo[0] if len(lo) > len(hi) else (hi[0] - lo[0]) / 2
    ret.append(median)
  return ret

def running_median(nums):
  left, right, ret = [], [], []
  median = float("inf")
  for num in nums:
    inversed = False
    if num < median:
      h, g = left, right
      num = -num
      inversed = True
    else:
      h, g = right, left
    
    if len(h) == len(g):
      heapq.heappush(h, num)
      median = -h[0] if inversed else h[0]
      ret.append(median)
    elif len(h) > len(g):
      heapq.heappush(g, -heapq.heappop(h))
      heapq.heappush(h, num)
      x, y = (-h[0], g[0]) if inversed else (h[0], -g[0])
      ret.append((x + y) / 2)
    else:
      heapq.heappush(h, num)
      x, y = (-h[0], g[0]) if inversed else (h[0], -g[0])
      ret.append((x + y) / 2)
  return ret


if __name__ == '__main__':
  nums = [2, 1, 5, 7, 2, 0, 5]
#   nums = [-1, 2, 0, 1, 0, 1, -1, -2]
  output = running_median(nums)
  print(output) # The output for the above example is [2 1.5 2 3.5 2 2 2].