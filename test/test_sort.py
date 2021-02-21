#!/usr/bin/env python3

import unittest
import sys
sys.path.insert(0, '../src')
from mergesort import mergesort
from quicksort import quicksort
from insertionsort import insertionsort

#arr = open('../src/input.txt', 'r').read().split('\n')
#arr = [x for x in arr if x]
arr = [int(x) for x in open('../src/input.txt', 'r').read().split('\n') if x]
my_sorted = [int(x) for x in open('../src/sorted.txt', 'r').read().split('\n') if x]

class TestSort(unittest.TestCase):
  def test_mergesort(self):
    self.assertEqual(mergesort(arr), my_sorted, None)

  def test_quicksort(self):
    self.assertEqual(quicksort(arr, 0, len(arr)-1), my_sorted, None)

  def test_insertionsort(self):
    self.assertEqual(insertionsort(arr), my_sorted, None)

if __name__ == '__main__':
  unittest.main()
