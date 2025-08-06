from queue import Queue
import copy
def solution(mat):
  '''
  Observation:
    (1). At every state of the matrix, we can pick a cell and flip it + 4 of its neighbors.
    (2). We can BFS on the state of the matric, make sure we dont visit the same state again.

  Algorithm:
    (1). Run BFS on state of the board.
    (2). At each state, we visit each cell in the matrix. Flip it + 4 of its neighbors. -> Generate new state.
    (3). Check if the new state has been visited or not, then put it into queue and continue to explore.

    Note: Since the state is unhashable, it is better to encode it as a string.

  Time: O(V + E), V (number of states) = 2^(MN) and E = MN * 2^(MN)
  Space: O(V)
  '''
  R, C = len(mat), len(mat[0])

  def encode(cur_mat: list[list[str]]) -> str:
    '''
    Given a current state of a board, convert it to a string (row1: string,row2: string)
    e.g: [[1, 0, 0],
          [0, 1, 0]]   --> '100,010'
    '''
    value = []
    for r in range(R):
      # convert this row to a string
      cur_row = ''.join(list(map(str, cur_mat[r])))
      value.append(cur_row)

    return ','.join(value)

  def decode(value: str) -> list[list[str]]:
    '''
    Given (row1, ..., rown), convert it back to the respective state of the board.
    e.g:  '100,010'   -->    [[1, 0, 0],
                              [0, 1, 0]]
    '''
    cur_mat = []
    rows = value.split(',')

    for r in range(R):
      cur_row = list(rows[r])
      cur_row = list(map(int, cur_row))
      cur_mat.append(cur_row)

    return cur_mat
  #-------------------------

  queue = Queue()
  dist = {}
  dr = [-1, 1, 0, 0]
  dc = [0, 0, 1, -1]

  start = encode(mat)
  end = encode([[0]*C for r in range(R)])

  queue.put(start)
  dist[start] = 0

  while queue.qsize()>0:
    state = queue.get()

    if state == end:
      return dist[state]

    cur_mat = decode(state)
    '''
    (1). Traverse through all cell
    (2). Flip it + 4 neighbors
    '''

    for r in range(R):
      for c in range(C):
        new_mat = copy.deepcopy(cur_mat)

        # flip (r,c)
        new_mat[r][c] = 1-new_mat[r][c]

        for i in range(4):
          new_r, new_c = r+dr[i], c+dc[i]

          if new_r in range(R) and new_c in range(C):
            # flip neighbor
            new_mat[new_r][new_c] = 1-new_mat[new_r][new_c]

        new_state = encode(new_mat)
        if new_state not in dist: # not explored yet
          dist[new_state] = dist[state] + 1
          queue.put(new_state)

  return -1
#-------------------------------------
mat = [[0,0],[0,1]]
print(solution(mat))



