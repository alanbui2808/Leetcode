from queue import Queue
import copy

def solution(graph):
  '''
  Observation:
    (1). We can visit the the same vertice multiple time, however when we visit again, our path (number of visited nodes so far) might
    or might not change.
    (2). Thus we use BFS on state = (X, path) where X is where we are and path is number of visited nodes so far arriving at X with
    an edge is simply the neighbor of X.
    (3). If we visit get ourself into the same (X, path) like before. We can ignore this. If we get into X again but with new_path != path.
    Then we have new state! (X, new_path)

  Algorithm:
    (1). Run BFS on state (X, path), path = TF..TF, path[v] = T means the path visits v
    (2). At each state (X, path):
      (2.1). Check all neighbors Y of X:
        - If Y not on the path, new_path = path + Y.
        - new_state = (Y, new_state).
        - Check if new_state is already been visited, put this state to queue and continue to explore respectively

  Note: Since this problem the state is complicated and unhashable by Python dict. Thus we convert it into a string.

  Time: O(V + E) where V (states) = V * 2^V states and E = V * (V*2^V). = V^2 *2^V, V = 12
  Space: O(V)

  '''
  def encode(v, path):
    '''
    Convert (v: int, path: [T,F]) into a string "v, TF..TF" - state
    '''
    path = ''.join(path)
    return str(v) + ',' + path

  def decode(value):
    '''
    Convert a string "v, TF..TF" to (v:int, path:[])
    '''
    v, path = value.split(',')
    path = list(path)
    return int(v), path
  #----------------------------------

  # dists = {state (string): total distance reach this state}
  dist = {}
  V = len(graph)

  queue = Queue()

  # Start our bfs at all v.
  # for v in range(V):
  for v in range(V):
    path = ['F' for v in range(V)]
    path[v] = 'T'
    state = encode(v, path)

    dist[state] = 0
    queue.put(state)

  while queue.qsize()>0:
    state = queue.get()

    u, path = decode(state)

    # this state has visited all the nodes.
    if 'F' not in path:
      return dist[state]

    for v in graph[u]:
      new_path = copy.copy(path)

      # If new state has not visited v
      if new_path[v] == 'F':
        new_path[v] = 'T'

      # encode this new_state
      new_state = encode(v, new_path)

      if new_state not in dist:
        dist[new_state] = dist[state] + 1
        queue.put(new_state)

  return
#--------------------------------------------------
graph = [[1,4],[0,3,4,7,9],[6,10],[1,10],[1,0],[6],[7,2,5],[6,1,8],[7],[1],[2,3]]
print(solution(graph))





