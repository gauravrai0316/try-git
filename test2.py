def incremet_items(L, increment):
   i = 0
   while i < len(L):
      L[i] = L[i] + increment
      i = i + 1

values = [1,2,3]
print(incremet_items(values, 2))
print(values)
