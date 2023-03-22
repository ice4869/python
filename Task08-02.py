x = input()
d = {}
for c in x:
  if c not in d:
    d[c] = 1
  else:
    d[c] = d[c] + 1
print(d)    
