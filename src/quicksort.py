#!/usr/bin/env python3
import fileinput

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
  return a

def main():
  arr = [int(line) for line in fileinput.input(files='input.txt')]
  print(quicksort(arr, 0, len(arr)-1))

if __name__ == '__main__':
  main()

