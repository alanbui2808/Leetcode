from queue import Queue

def solution(recipes, ingredients, supplies):
  '''
  Algorithm: Topological sorting.
  (1). We construct a graph where v --> u means u is made of v.
  (2). Record the indegree of all nodes.
  (3). We run topological sort from ingredients inside supplies
    (3.1). when indegree[u] reaches 0 and u in recipes then we add to the result list.
    (3.2). TS continues to explore and pop all u with indegree[u] = 0.
      (3.3). for all v in u: update indegree[v] -= 1

  Visually:
    yeast --> bread <-- flour
  we start by having indegree[yeast] = 0 and indegree[flour] = 0, pop these 2 nodes out
  and update indegree[bread] = 0 and the graph becomes:

    bread

  In the next iteration then indegree[bread] = 0 and bread is in recipe then we add bread
  to the result list

  Time Complexity: O(V + E) (similar to BFS) where V is the number of ingredients
  and E = ingredients[i].length = 100 * number of recipes = 100*N
  Overall the algorithm is O(N + N) = O(N)
  '''
  queue = Queue()
  indegree, graph = {}, {}

  for i in range(len(recipes)):
    u, v = recipes[i], ingredients[i]

    if u not in graph:
      graph[u] = []
      indegree[u] = 0

    for x in v:
      if x not in graph:
        graph[x] = []
        indegree[x] = 0

      graph[x].append(u) # x --> u
      indegree[u] += 1 # update indegree

  for u in indegree.keys():
    # u is the most basic ingredient and not in supply
    # we mark indegree of u to be inf (not available)
    if indegree[u] == 0 and u not in supplies:
      indegree[u] = float('inf')
    if indegree[u] == 0 and u in supplies:
      queue.put(u)

  result = []
  # Topological Sort
  while not queue.empty():
    u = queue.get()
    # if u is in recipes
    if u in recipes:
      result.append(u)

    for v in graph[u]:
      # decrease the indegree of the neighbors
      indegree[v] -= 1
      if indegree[v] == 0:
        queue.put(v)

  return result


recipes = ["bread"]
ingredients = [["yeast","flour"]]
supplies = ["yeast","flour","corn"]
print(solution(recipes, ingredients, supplies))






