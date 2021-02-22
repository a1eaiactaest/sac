#!/usr/bin/env python3
import fileinput
"""
def insertionsort(a,n):   # recursive
  if n > 0:
    insertionsort(a, n-1)
    t = a[n]
    i = n-1
    while i >=0 and a[i] > t:
      a[i+1] = a[i]
      i -= 1
    a[i+1] = t

"""

# had to change to iterative because recursive did not work

def insertionsort(a):
  for i in range(1, len(a)):
    k = a[i]
    j = i-1
    while j >= 0 and k < a[j]:
      a[j+1] = a[j]
      j -= 1
    a[j+1] = k
  return a

def main():
  arr = [int(line) for line in fileinput.input(files='input.txt')]
  print(insertionsort(arr))

if __name__ == '__main__':
  main()
