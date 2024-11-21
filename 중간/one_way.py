def one_away(s1, s2):
  # TODO
  if not s1 or not s2:
    return False
  if len(s1) < len(s2):
    s1, s2 = s2, s1
  if len(s1) - len(s2) > 1:
    return False
  if len(s1) == len(s2):
    #same or replace
    cnt = 0
    for i in range(len(s1)):
      if s1[i] != s2[i]:
        cnt += 1
    return cnt <= 1
  else:
    #insert or delete
    cnt = idx1 = idx2 = 0
    while idx1 < len(s1) and idx2 < len(s2):
      if s1[idx1] != s2[idx2]:
        if cnt == 1:
          return False
        cnt += 1
        idx1 += 1
      else:
        idx1 += 1
        idx2 += 1
    return cnt <= 1


if __name__ == '__main__':
  lists = list(input().split())
  print(one_away(lists[0], lists[1]))