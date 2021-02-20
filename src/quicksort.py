#!/usr/bin/env python3

def partition(a, l, h): # array, low, high
  piv = a[h] # set pivoot

  left=l-1
  for i in range(l, h):
    if a[i] <= piv:
      left += 1
      # swap(a[left], a[i])
      (a[left], a[i]) = (a[i], a[left])

  (a[left+1], a[h]) = (a[h], a[left+1])
  return left+1

def quicksort(a, l, h):
  if l<h:
    piv_loc = partition(a, l, h) # locate pivot
    quicksort(a, l, piv_loc-1)
    quicksort(a, piv_loc+1, h)

a = [1160, 563, 916, 736, 658, 81, 1104, 302, 787, 58, 1220, 1149]
quicksort(a, 0, len(a)-1)
print(a)

