from collections import deque

class Node:
  def __init__(self, moves, position, speed):
    self.moves, self.position, self.speed = moves, position, speed

def solution(target):
  '''
  Algorithm:
  (1). BFS on the state where state = (moves, position, speed)
  (2). When we consider each state, we have 2 options:
    (2.1). Accelerate by speed to new state (moves+1, position+speed, speed*2)
    (2.2). Reverse if the next move (children) pass the target (either below or above).
        The new state is (moves+1, position, speed={-1, 1})

  The reason why we need to save the state info is because we want to avoid revisting the node again.

  Time complexity: BFS is determined by our states - all combination of (position, speed) we can reach.
  We know there is a limit to our position, by line 38, soon we overshoot it will reverse immediate, we in the worst
  case we will visit [-target, target] position. O(T)

  Speed goes by 2 everytime until we reach target, thus O(log(T))

  O(T*log(T))
  '''
  queue = deque()
  queue.append(Node(0, 0, 1))
  visited = set()
  visited.add((0, 1))

  while queue:
    node = queue.popleft()
    moves, position, speed = node.moves, node.position, node.speed

    if position == target:
      return moves

    # Accelerate by "A"
    if (position+speed, speed*2) not in visited:
      queue.append(Node(moves+1, position+speed, speed*2))
      visited.add((position+speed, speed*2))

    # Check if next state overshoot us in order to reserve
    if (position + speed > target) or (position + speed < target):
      speed = -1 if speed > 0 else 1
      # Reverse and keep the position
      if (position, speed) not in visited:
        visited.add((position, speed))
        queue.append(Node(moves+1, position, speed))



target = int(input())
print(solution(target))


