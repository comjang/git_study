import matplotlib.pyplot as plt
import random as r
x = []
n = 10000
m = 5
for _ in range(n):
  sum = 0
  for _ in range(m):
    sum += r.randrange(1, 7)
  x.append(sum)
plt.hist(x, bins=5*m)
plt.show()
