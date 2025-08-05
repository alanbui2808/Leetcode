import heapq
from collections import Counter

def solution(s):
  '''
  Observation: Use Counter and Heap

  Time: O(26log26 + N)
  '''
  N = len(s)
  res = []

  cnt = Counter(s)
  heap = [(-freq, char) for char, freq in cnt.items()]
  heapq.heapify(heap)

  while heap:
    freq, char = heapq.heappop(heap)
    freq *= -1
    res.append(char*freq)

  return ''.join(res)
#-------------------------------
s = "tree"
print(solution(s))
s = "cccaaa"
print(solution(s))
s = "Aabb"
print(solution(s))


