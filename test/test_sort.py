#!/usr/bin/env python3

import unittest
import sys
sys.path.insert(0, '../src')
from mergesort import mergesort
from quicksort import quicksort

#arr = open('../src/input.txt', 'r').read().split('\n')
#arr = [x for x in arr if x]
arr = [x for x in open('../src/input.txt', 'r').read().split('\n') if x]
my_sorted = [x for x in open('../src/sorted.txt', 'r').read().split('\n') if x]

class 
