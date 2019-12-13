# Dynamic Programming
#  - Longest Common Subsequence (LCS)

import numpy as np

X = np.array(['b', 'c', 'd', 'b', 'c', 'd', 'a'])
Y = np.array(['a', 'b', 'e', 'c', 'b', 'a'])
n = len(X)
m = len(Y)

def LCS(X, Y, n, m):
  L = np.zeros(shape=(n+1,m+1), dtype=int)
  # base case
  for i in range(n+1):
    L[i][0] = 0
  for j in range(m+1):
    L[0][j] = 0
  for i in range(1, n+1, 1):
    for j in range(1, m+1, 1):
      if X[i-1] == Y[j-1]:      # ending elements are same
        L[i][j] = 1 + L[i-1][j-1]
      else:                       # ending elements are different
        L[i][j] = max(L[i-1][j], L[i][j-1])
  print(L)
  return(L[n][m])
    

print(LCS(X,Y,n,m))
    
