#!/usr/bin/env python3

def bubblesort(a):
  for i in range(len(a)-1):
    swp = 0 # False
    for j in range(len(a)-i-1):
      if a[j] > a[j+1]:
        (a[j+1], a[j]) = (a[j], a[j+1])
        swp = 1 # True
    if swp == 0:
      break
  return a

arr = [1160, 563, 916, 736, 658, 81, 1104, 302, 787, 58, 1220, 1149]
bubblesort(arr)
print(arr)
