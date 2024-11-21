import heapq

def running_median(nums):
  ret = []
  largeQ = [] #minQ
  smallQ = [] #maxQ
  for num in nums:
    if len(smallQ) <= len(largeQ):
      #push to smallQ
      if largeQ and largeQ[0] < num:
        tmp = heapq.heappop(largeQ)
        heapq.heappush(smallQ, -tmp)
        heapq.heappush(largeQ, num)
      else:
        heapq.heappush(smallQ, -num)
    else:
        #push to largeQ
        if smallQ and -smallQ[0] > num:
          tmp = -heapq.heappop(smallQ)
          heapq.heappush(largeQ, tmp)
          heapq.heappush(smallQ, -num)
        else:
          heapq.heappush(largeQ, num)
    median = -smallQ[0] if len(smallQ) > len(largeQ) else (-smallQ[0] + largeQ[0]) / 2
    ret.append(median)
  return ret

if __name__ == '__main__':
  nums = [2, 1, 5, 7, 2, 0, 5]
  # nums = [-1, 2, 0, 1, 0, 1, -1, -2]
  output = running_median(nums)
  print(output) # The output for the above example is [2 1.5 2 3.5 2 2 2].