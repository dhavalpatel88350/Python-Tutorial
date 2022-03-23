n = [2, 1, 5, 6, 3]
for i in range(len(n)):
      s = 0
      for i in range(1, i+1):
         if n[i] > n[s]:
            s = i
      temp = n[i]
      n[i] = n[s]
      n[s] = temp
print(n)
