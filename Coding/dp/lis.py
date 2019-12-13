# Dynamic Programming
#  - Longest Increasing Subsequence (LIS)

# 1. Define the subproblem a1, a2, ..., ai & including ai.
# 2. State the recurrence using the subproblems

import numpy as np

a = [5, 7, 4, -3, 9, 1, 10, 4, 5, 8, 9, 3]
n = len(a)

def LIS(a, n):
  L = [1] * n #Table to store subproblem results
  for i in range(n):
     print i, L
     for j in range(0, i, 1):
       if a[j] < a[i] and L[i] < (1+L[j]):
         L[i] = 1 + L[j]
  max = 0
  for i in range(n):
    if L[i] > L[max]:
      max = i
  print a
  print L
  return L[max]

print LIS(a, n)
