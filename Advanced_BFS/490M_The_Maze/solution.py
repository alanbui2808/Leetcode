from queue import Queue

def solution(maze, start, destination):
  '''
  Observation:
    (1). At each position where the ball currently resigns, we need to save a state (r, c, d) where d is the current direction.
    (2). We have 2 options:
      (2.1). Hit a wall or source node: Then we need to change direction.
      (2.2). Else we continue to do so.

    (3). Like simple unweighted bfs, we update dist[r][c]

  HOWEVER: Our state is (r, c, d) instead of simple (r, c). This means even though the ball may resigns in the next position that
  might have been visited, we can still explore the path if dist[r][c][d] has never been explored.

  Time: O(V + E), V (number of states): MN*4, E = 4 * V = MN*16
  Space: O(V)

  '''
  R, C = len(maze), len(maze[0])

  # visited = {(r, c, dir): T/F}
  visited = {}
  dest_r, dest_c = destination
  start_r, start_c = start

  # initialization
  visited[(start_r, start_c, -1)] = True
  queue = Queue()
  queue.put((start_r, start_c, -1))

  # (up, down, left, right)
  dr = [1, -1, 0, 0]
  dc = [0, 0, -1, 1]


  def get_wall_hitted(r, c, d):
    '''
    Given r, c, d check new direction along d direction hits a wall or not
    '''
    new_r, new_c = r+dr[d], c+dc[d]
    return new_r not in range(R) or new_c not in range(C) or maze[new_r][new_c] == 1


  while queue.qsize()>0:
    r, c, d = queue.get()
    wall_hitted = get_wall_hitted(r, c, d)

    # reach target node and it's against the wall
    if (r, c) == (dest_r, dest_c) and wall_hitted:
      return visited[(dest_r, dest_c, d)]

    # At start position or we hit a wall (including the border)
    if (r, c) == (start_r, start_c) or wall_hitted:

      # Change direction
      for i in range(4):
        # ignore the next pos where it hits the wall
        if i == d: continue

        new_r, new_c = r+dr[i], c+dc[i]

        if new_r in range(R) and new_c in range(C) and maze[new_r][new_c] != 1 and (new_r, new_c, i) not in visited:
          # Encounter new state
          visited[(new_r, new_c, i)] = True
          queue.put((new_r, new_c, i))

    else:
      # we already check if this new pos along with direction hits a wall or not so we not need to check
      new_r, new_c = r+dr[d], c+dc[d]

      if (new_r, new_c, d) not in visited:
        queue.put((new_r, new_c, d))
        visited[(new_r, new_c, d)] = True

  return -1
#-------------------------------------------------------
maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]
start = [0,4]
destination = [3,2]
print(solution(maze, start, destination))


