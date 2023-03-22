x = (input())
if not x.isdigit():
   print(f"{x} 是一個不合法的輸入，無法運算。")
    
else:
  factorial = 1
  for i in range(int(x)+1):
   if i == 0:
     continue
   factorial = i*factorial
  print(factorial)
