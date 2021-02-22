#/usr/bin/env python3

import unittest
import fileinput
import sys
sys.path.insert(0, '../src')
from mergesort import mergesort
from quicksort import quicksort
from insertionsort import insertionsort
from selectionsort import selectionsort
from bubblesort import bubblesort

#arr = open('../src/input.txt', 'r').read().split('\n')
#arr = [x for x in arr if x]
my_sorted = [int(y) for y in fileinput.input(files='../src/sorted.txt')]
#arr = [5,9,1,3,4,6,6,3,2]
#my_sorted = [1,2,3,3,4,5,6,6,9]
class TestSort(unittest.TestCase):
  def test_mergesort(self):
    arr = [int(x) for x in fileinput.input(files='../src/input.txt')]
    self.assertEqual(mergesort(arr), my_sorted)

  def test_quicksort(self):
    arr = [int(x) for x in fileinput.input(files='../src/input.txt')]
    self.assertEqual(quicksort(arr, 0, len(arr)-1), my_sorted)

  def test_insertionsort(self):
    arr = [int(x) for x in fileinput.input(files='../src/input.txt')]
    self.assertEqual(insertionsort(arr), my_sorted)

  def test_selectionsort(self):
    arr = [int(x) for x in fileinput.input(files='../src/input.txt')]
    self.assertEqual(selectionsort(arr), my_sorted)

  def test_bubblesort(self):
    arr = [int(x) for x in fileinput.input(files='../src/input.txt')]
    self.assertEqual(bubblesort(arr), my_sorted)

if __name__ == '__main__':
  unittest.main()
