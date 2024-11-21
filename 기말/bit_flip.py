def num_bits_to_flip(a, b):
  bitlen = 0
  hi = max(a, b)
  while hi:
    bitlen += 1
    hi >>= 1
  res = a ^ b
  ret = 0
  for i in range(bitlen):
    if ((res >> i) & 1):
       ret += 1
  return ret


if __name__ == '__main__':
  a = 29
  b = 15
  output = num_bits_to_flip(a, b)
  print(output) # The output for the above example is 2.
