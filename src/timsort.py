#!/usr/bin/env python3
#https://github.com/python/cpython/blob/master/Objects/listobject.c

import fileinput

# modify insertionsort
"""
df insertionsort(a, l=0, r=None):
  if r is None:
    r = len(a)-1
  for i in range(l+1, r+1):
    k = a[i]
    j = i-1
    
    while k >= l and a[j] > k:
      a[j+1] = a[j]
      j -= 1
    a[j+1] = k
  return a

def merge(m1, m2):
  if len(m1) == 0:
    return m2
  if len(m2) == 0:
    return m1

  res = []
  m1 = 0
  m2 = 0
  while True:
    if len(res) < len(l) + len(r):


def timsort(a): #sorted()
  mr = 32 # slicing
  
  for i in range(0, n, mr):
    insertionsort(a, i, min((i+mr-1), len(a)-1))

    s = mr
    while s < len(a):
      for begin in range(0, len(a), s*2):
        piv = begin + s - 1
"""
def timsort(a):
  return sorted(a)

def main():
  arr = [int(line) for line in fileinput.input(files='input.txt')]
  print(timsort(arr))

if __name__ == '__main__':
  main()
