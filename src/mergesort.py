#!/usr/bin/env python3

def mergesort(a):
  if len(a) == 1:
    return a
  elif len(a) == 2:
    if a[0] > a[1]:
      return [a[1], a[0]]
    else:
      return a

  piv = len(a)//2
  m1 = mergesort(a[:piv])
  m2 = mergesort(a[piv:])

  acc = []
  while True:
    if len(m1) > 0 and len(m2) > 0:
      if m1[0] > m2[0]:
        acc.append(m2[0])
        m2 = m2[1:]
      else:
        acc.append(m1[0])
        m1 = m1[1:]
    elif len(m1) > 0:
      acc.append(m1[0])
      m1 = m1[1:]
    elif len(m2) > 0:
      acc.append(m2[0])
      m2 = m2[1:]
    else:
      break
  return acc
					
if __name__ == '__main__':        
  arr = [1160, 563, 916, 736, 658, 81, 1104, 302, 787, 58, 1220, 1149]
  print(mergesort(arr))
