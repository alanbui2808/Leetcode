import heapq

def solution(nums1, nums2, k):
  '''
  Observation: BFS + Priority Queue (kinda similar to Dijkstra)

  Algorithm: We know pair (0,0) has the smallest sum. Initialize visited[(i,j)] and min_heap[(sum, i, j)]
  We start at pair (0,0).

    (1). For each (i, j) popped out the heap. Append it to res[(i, j)]
    (2). Note: Whenever a node is popped out the heap we know it's the smallest. Proof from Dijkstra algorithm
    (3). Explore (i+1, j) and (i, j+1). Push them into the queue if they are visited aka (i+1, j) or (i, j+1) hasnt been
    visited/pushed into the heap yet.


  Time: min(K + KlogK, V + VlogV) where V = total of vertices or N*M
    => K+KlogK: Each iteration, we pop 1 vertice out and append at most 2 vertices in

  Space: min(K, V)
  '''
  N = len(nums1)
  M = len(nums2)
  min_heap = []
  visited = {}

  heapq.heappush(min_heap, (nums1[0]+nums2[0], 0, 0))
  visited[(0, 0)] = 1
  res = []
  di = [1,0]
  dj = [0,1]

  while min_heap and len(res)<k:
    _, i, j = heapq.heappop(min_heap)
    res.append((nums1[i], nums2[j]))

    for d in range(len(di)):
      new_i, new_j = i+di[d], j+dj[d]

      if new_i<N and new_j<M and (new_i, new_j) not in visited:
        new_dist = nums1[new_i]+nums2[new_j]

        heapq.heappush(min_heap, (new_dist, new_i, new_j))
        visited[(new_i, new_j)] = 1

  return res
#-------------------------------------------
nums1 = [1,7,11]
nums2 = [2,4,6]
k = 3
print(solution(nums1, nums2, k))
nums1 = [1,1,2]
nums2 = [1,2,3]
k = 2
print(solution(nums1, nums2, k))
nums1 = [1,2,4,5,6]
nums2 = [3,5,7,9]
k = 20
print(solution(nums1, nums2, k))
