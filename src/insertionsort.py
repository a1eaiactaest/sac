#!/usr/bin/env python3

def insertionsort(a,n):
  if n>0:
    insertionsort(a, n-1)
    t = a[n]
    i = n-1
    while i >=0 and a[i] > t:
      a[i+1] = a[i]
      i -= 1
    a[i+1] = t

arr = [1160, 563, 916, 736, 658, 81, 1104, 302, 787, 58, 1220, 1149]
insertionsort(arr, len(arr)-1)
print(arr)
