import sys

# def fewest_number(bricks):
#   lo = height = len(bricks)
#   cnts = {}
#   for line in bricks:
#     length = 0
#     for i, brick in enumerate(line):
#       length += brick
#       if (i != len(line) - 1):
#         cnts[length] = 1 if length not in cnts else cnts[length] + 1
    
#   for cnt in cnts.values():
#       lo = min(lo, height - cnt)
#   return lo

def fewest_number(bricks) -> int:
  cnts = {}
  for line in bricks:
    ssum = 0
    for curr in line[:-1]:
      ssum += curr
      if ssum in cnts:
        cnts[ssum] += 1
      else:
        cnts[ssum] = 1
  
  if not cnts:
    return 0
  
  return len(bricks) - max(cnts.values())



def test():
  height = 6
  bricks = [
    [3, 5, 1, 1], [2, 3, 3, 2], [5, 5], [4, 4, 2], [1, 3, 3, 3], [1, 1, 6, 1, 1]
  ]
  # bricks = [[5], [5]]
  n = fewest_number(bricks)
  print(n)
  # print(n) # The output for the above example is 2.

if __name__ == '__main__':
  test()

