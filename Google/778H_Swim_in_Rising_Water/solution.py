from queue import PriorityQueue

# class Entry:
#   def __init__(self, cost, r, c):
#     self.cost = cost
#     self.r, self.c = r, c

#   def __lt__(self, other):
#     return self.cost < other.cost


# def solution(grid):
#   '''
#   Run Dijkstra algorithm

#   Time complexity: O(V + Elog(E)) --> O(N^2 log(N^2)) = O(N^2 2*log(N))

#   '''
#   N = len(grid)
#   pq = PriorityQueue()
#   visit = set()
#   pq.put(Entry(grid[0][0], 0, 0))
#   cost = [[0 for i in range(N)] for j in range(N)]
#   dr = [1, -1, 0, 0]
#   dc = [0, 0, -1, 1]


#   while not pq.empty():
#     # Once an entry is popped outside the pq then its guaranteed to be the shortest path to this entry
#     node = pq.get()
#     cst, r, c = node.cost, node.r, node.c
#     visit.add((r, c))
#     cost[r][c] = cst

#     if (r, c) == (N-1, N-1):
#       break

#     for i in range(4):
#       new_r, new_c = r + dr[i], c + dc[i]

#       # We found a node that has not been visited (popped out the heap)
#       if new_r in range(N) and new_c in range(N) and (new_r, new_c) not in visit:
#         # We calculate the cost to reach (new_r, new_c)
#         # If the gets to the parent node > the water level of (new_r, new_c) then we the cost to reach (new_r, new_c) must be cost[parent]
#         # Else then the cost gets to (new_r, new_c) = water level of (new_r, new_c)
#         new_cost = max(cst, grid[new_r][new_c])
#         pq.put(Entry(new_cost, new_r, new_c))

#   return cost[-1][-1]

#=================================================
from queue import Queue

def solution(grid):
  '''
  Observation:
    - Minimize maximal path, we can use bin search.
    - Guess an elevation, perform BFS to check if we can reach (0,0) to (n-1, n-1) within given elevation

  Algorithm
    (1). Bin search on [grid[0][0], max(grid)]. We need grid[0][0] because we must always start at elevation of (0,0)
    (2). If we can reach, reduce the search space for elevation.

  Time: O(N^2logN), BFS: (N^2)
  '''
  n = len(grid)

  def check(target):
    queue = Queue()
    visited = [[False]*n for _ in range(n)]
    queue.put((0,0))
    visited[0][0] = True

    dr = [-1, 1, 0, 0]
    dc = [0, 0, 1, -1]

    while queue.qsize()>0:
      r, c = queue.get()

      if (r, c) == (n-1, n-1):
        return True

      for i in range(4):
        new_r, new_c = r+dr[i], c+dc[i]

        if new_r in range(n) and new_c in range(n) and not visited[new_r][new_c] and grid[new_r][new_c] <= target:
          visited[new_r][new_c] = True
          queue.put((new_r, new_c))

    # Cannot swim from (0,0) to (n-1, n-1) with this level of elevation
    return False
  #---------------------------------------
  L, R = 0, 50**2
  result = R

  while L <= R:
    mid = L + (R-L)//2

    if check(mid):
      result = mid
      R = mid-1
    else:
      L = mid+1

  return result
#------------------------------------------------------
grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
print(solution(grid))
