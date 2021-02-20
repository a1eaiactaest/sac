#!/usr/bin/env python3
import fileinput

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

def main():
  arr = [int(line) for line in fileinput.input(files='input.txt')]
  bubblesort(arr)
  print(arr)

if __name__ == '__main__':
  main()
