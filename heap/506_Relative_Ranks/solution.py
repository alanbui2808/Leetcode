import heapq

def solution(scores):
  N = len(scores)
  res = [i+1 for i in range(N)]

  max_heap = [(-score, idx) for idx, score in enumerate(scores)]
  heapq.heapify(max_heap)
  pos = 1
  title = None

  while max_heap:
    neg_score, idx = heapq.heappop(max_heap)

    if pos==1:
      title = "Gold Medal"
    elif pos==2:
      title = "Silver Medal"
    elif pos==3:
      title = "Bronze Medal"
    else:
      title = str(pos)

    res[idx] = title
    pos += 1

  return res
#-------------------------------------
scores = [5,4,3,2,1]
print(solution(scores))
scores = [10,3,8,9,4]
print(solution(scores))
