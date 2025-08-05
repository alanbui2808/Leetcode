from heapq import heapify, heappop, heappush
from collections import Counter

def solution(tasks, n):
  '''
  Observation: Heap
    1. At each t, we look for task with earliest start time available.

  Algorithm:
    1. Construct min_heap of (start, task) where start: 1, 1+n+1, 1+2(n+1), etc

    Start with t = 1
    2. For every iteration:
      - Pop the top element (start, task).
      - If start time <= t, update t += 1
      - Otherwise: t = start+1 meaning we must idle until start.

    3. return t-1

  Time: O(NlogN)
  Space: O(N)
  '''
  N = len(tasks)
  cnt = Counter(tasks)

  min_heap = []

  # construct min_heap with Counter(char: freq)
  for task, freq in cnt.items():
    start = -n

    for i in range(freq):
      start += (n+1)
      heappush(min_heap, (start, task))

  res = 1
  while min_heap:
    start, _ = heappop(min_heap)

    if res >= start:
      res += 1

    else:
      res = start+1

  return res-1

#--------------------------
tasks = ["A","A","A","B","B","B"]
n = 2
print(solution(tasks, n))

tasks = ["A","C","A","B","D","B"]
n = 1
print(solution(tasks, n))

tasks = ["A","A","A", "B","B","B"]
n = 3
print(solution(tasks, n))

