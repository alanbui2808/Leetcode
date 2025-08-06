from queue import Queue

def solution(richer, quiet):
  '''
  Observation:
    (1). There are dependencies, we must use topo sort.
    (2). Given a topological order, s.t v > u. It is ambigious if v indeed has more money than u. In the first example:
      A possible topo order is: 4 5 6 2 3 7 1 0. 7 is def quieter than 5 but we dont know 7 indeed has more money than 0. Thus the person
      has more money than 0 must be able to reach 0 (there exists a path from that person to 0)

    (3). When we process BFS (toposorting) by popping u from a queue and decrement indegree of all its v. We can pass the information of the current
    person that is richer and least quiet than u to v (pass the information from the parent, great parents, etc to the current child). Example:

          2 -> 1 <--3
               |
          4 -> 5 <--6

      By the first iteration, the information will flow into (1). (1) now store the person richer and least quiet from both (2) and (3).
      By the second iteration, the information will flow into (5). (5) now store the person richer and least quiet from both (1), (4) and (5)

      Note that, (6) and (4) is topologically smaller than (2), (3) and (1) but the information from those never reach.

  Algorithm:
    (1). Intialize result = {person_x: (person_y, quiet_y)}
    (1). Run BFS topological sorting.
    (2). At u, process v:
        (2.1). result[v] = min(result[v], result[u])

  Time: O(N^2)
  Space: O(N^2)
  '''
  n = len(quiet)
  # {person_x: (person_y, quiet_y)}
  # records the current person_y who is richer than person_x and least quiet.
  result = [i for i in range(n)]

  graph = [[] for _ in range(n)]
  indegree = [0 for _ in range(n)]


  for u, v in richer:
    graph[u].append(v)
    indegree[v] += 1


  queue = Queue()

  for v in range(n):
    if indegree[v] == 0:
      queue.put(v)


  while queue.qsize()>0:
    u = queue.get()

    for v in graph[u]:
      indegree[v] -= 1
      if indegree[v] == 0:
        queue.put(v)

      # the information of vertices with greater order is flown into this v.
      # parent of u is quieter than parent of v. Parent here means the richer person.
      if quiet[result[u]] < quiet[result[v]]:
        result[v] = result[u]

  return result

#----------------------------
richer = [[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]]
quiet = [3,2,5,4,6,1,7,0]
print(solution(richer, quiet))
