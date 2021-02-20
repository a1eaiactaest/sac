#!/usr/bin/env python3

def selectionsort(a):
  for i in range(len(a)):
    min_i = i
    for j in range(i+1, len(a)):
      if a[min_i] > a[j]:
        min_i = j
    (a[i], a[min_i]) = (a[min_i], a[i])

arr = [1160, 563, 916, 736, 658, 81, 1104, 302, 787, 58, 1220, 1149]
selectionsort(arr)
print(arr)
