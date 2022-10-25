a = int(input())
b = int(input())
if b == 0:
  print('не делится на 0')
elif a % b ==0:
  print('делится', a // b)
else:
  print('не делится', a % b)
  