from heapq import heappush, heappop, heapify

def solution(k, w, profits, capitals):
  '''
  Observation: Greedy
    - Always pick the project with maximal project but capital <= cur_cap at every iteration.
    - Use max_heap to quickly determine the job.

  Algorithm 1:
    1. Construct max_heap of (profit, capital)
    2. Every iteration:
      - pop max_heap until we found the right one, put those unsuitable in a temp[]
      - push back those projects in temp[] back to max_heap
    => inefficient, basically 2logN operations.

  Algorithm 2:
    1. Sort projects (capital, project) by capital.
    2. Every iteration:
      - Collect all the projects with capital <= cur_capital using a pointer.
      - Push those projects into max_heap.
      - Now we can pop the top element of max_heap.

    => So each iteration, it's O(C + logN) only where C is a constant.

  Time: O(KlogN)
  Space: O(N)
  '''
  N = len(profits)
  res = w

  # sort by capitals (ascending)
  projects = list(zip(capitals, profits))
  projects.sort()

  # ptr to collect projects
  ptr = 0
  max_heap = []

  for i in range(k):
    # collect all projects with c <= cur_cap
    while ptr < N and projects[ptr][0]<=res:
      heappush(max_heap, -projects[ptr][1])
      ptr += 1

    if not max_heap:
      break

    res += -heappop(max_heap)

  return res
#-------------------------------------------
k = 2
w = 0
profits = [1,2,3]
capitals = [0,1,1]
print(solution(k, w, profits, capitals), "expected: 4")

k = 3
w = 0
profits = [1,2,3]
capitals = [0,1,2]
print(solution(k, w, profits, capitals), "expected: 6")
