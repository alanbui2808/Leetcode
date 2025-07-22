from collections import defaultdict

def solution(n, logs, queries, x):
  '''
  Observation:
    (1). First we sort logs and queries by time in increasing order.
    (2). For each query: (start, end)
      => Find the largest window in logs such that all the time within (start, end)
      => [L, R]: While expand this window remember to record how many servers in total.
      => thus result = total_server - used_servers


  Time: O(NlogN + MlogM) where N = len(logs) and M = len(queries)
  Space: O(M)
  '''
  N = len(logs)
  M = len(queries)
  L, R = 0, 0
  count = defaultdict(int)
  result = [0]*M

  # sort logs and queries by t
  logs.sort(key=lambda l: l[1])
  # [(query, id)] so we can add result to correct idx
  queries = sorted([t, id] for id, t in enumerate(queries))

  for t, id in queries:
    # expand R until the current server has time > t
    while R < N and logs[R][1] <= t:
      count[logs[R][0]] += 1
      R += 1

    # shrink L until the server has time <= t
    while L < R and logs[L][1] < t-x:
      count[logs[L][0]] -= 1

      # remove the server if count[server]==0
      if count[logs[L][0]] == 0:
        del count[logs[L][0]]

      L += 1

    # [L, R-1] is now valid
    result[id] = n - len(count)

  return result
#---------------------------------------
n = 3
logs = [[1,3],[2,6],[1,5]]
x = 5
queries = [10,11]
print(solution(3, logs, queries, x), ', expected: [1,2]')
logs = [[2,4],[2,1],[1,2],[3,1]]
x = 2
queries = [3,4]
print(solution(3, logs, queries, x), ', expected: [0,1]')

