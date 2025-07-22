from queue import Queue

class TreeNode:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left, self.right = left, right

def solution(root):
  '''
  Algorithm:
  (1). BFS to construct a graph and record indegree of all node
  (2). Run topological sorting

  Time Complexity: O(E + V): E = V-1 since it's a tree so overall O(N)
  '''
  def bfs(root):
    queue = Queue()
    queue.put(root)
    graph[root] = []

    while not queue.empty():
      # keep track of level
      level_size = queue.qsize()

      for i in range(level_size):
        node = queue.get()
        indegree[node] = 0

        if node.left:
          queue.put(node.left)
          graph[node.left] = [node] # children --> node, [node] is for generalization
          indegree[node] += 1
        if node.right:
          queue.put(node.right)
          graph[node.right] = [node] # children --> node
          indegree[node] += 1

  graph, indegree = {}, {}
  result = []
  bfs(root)

  queue = Queue()

  for u in graph:
    if indegree[u] == 0:
      queue.put(u)

  while not queue.empty():
    # we also need to keep track of each level
    level_size = queue.qsize()
    level = []
    for i in range(level_size):
      u = queue.get()

      level.append(u.value)

      for v in graph[u]: # check if u has parent
        indegree[v] -= 1
        if indegree[v] == 0:
          queue.put(v)

    result.append(level)

  return result
#-----------------------------------------------
one = TreeNode(1)
two = TreeNode(2)
three = TreeNode(3)
four = TreeNode(4)
five = TreeNode(5)

one.left, one.right = two, three
two.left, two.right = four, five

print(solution(one))

