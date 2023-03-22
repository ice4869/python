x = int(input())
factorial = 1
sum = 0

for i in range(x+1):
  if i == 0:
    continue
  factorial = factorial*i
  sum = sum + factorial
print(sum)
