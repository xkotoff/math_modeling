b0 = int(input())
q = int(input())
n = int(input())

for iter in range(0, n, 1):
  print(f'iteration: {iter}')
  bn = b0 * q
  print(bn)
  b0 = bn
