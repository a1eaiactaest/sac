#!/usr/bin/env python3

import fileinput

def selectionsort(a):
  for i in range(len(a)):
    min_i = i
    for j in range(i+1, len(a)):
      if a[min_i] > a[j]:
        min_i = j
    (a[i], a[min_i]) = (a[min_i], a[i])
  return a

def main():
  arr = [int(x) for x in fileinput.input(files='input.txt')]
  print(selectionsort(arr))
 
if __name__ == '__main__':
  main()
