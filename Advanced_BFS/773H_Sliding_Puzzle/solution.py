from queue import Queue
import copy

def solution(board):
  '''
  Observation:
    (1). At every state of the board, we can slide the 0 cell to its neighbor.
    (2). We can BFS on the state of the board, make sure we dont visit the same state again.

  Algorithm:
    (1). Run BFS on state of the board.
    (2). At each state, consider swapping 0 cell to its neighbor.
    (3). Check if the new state has been visited or not, then put it into queue and continue to explore.

    Note: Since the state is unhashable, it is better to encode it as a string.

  Time: O(V + E), V (number of states) = 6! and E = 3*V = 3 * 6! = 720
  Space: O(V)
  '''
  R, C = 2, 3

  def encode(cur_board: list[list[str]]) -> str:
    '''
    Given a current state of a board, convert it to a string (row1: string,row2: string)
    e.g: [['1', '2', '3'],
          ['4', '5', '0']]   --> '123,450'
    '''
    value = []
    for r in range(R):
      # convert this row to a string
      cur_row = ''.join(cur_board[r])
      value.append(cur_row)

    return ','.join(value)

  def decode(value: str) -> list[list[int]]:
    '''
    Given (row1: string, row2: string), convert it back to the respective state of the board.
    e.g:  '123,450'   -->    [['1', '2', '3'],
                              ['4', '5', '0']]
    '''
    cur_board = []

    row1, row2 = value.split(',')
    row1 = list(row1)
    row2 = list(row2)
    cur_board.append(row1)
    cur_board.append(row2)

    return cur_board

  def find_zero(cur_board):
    for r in range(R):
      for c in range(C):
        if cur_board[r][c] == '0':
          return r, c

  #----------------------------------
  queue = Queue()
  dist = {}
  dr = [-1, 1, 0, 0]
  dc = [0, 0, -1, 1]

  # Convert board[r][c] to str instead
  for r in range(R):
    board[r] = list(map(str, board[r]))

  start = encode(board)
  end = encode([['1', '2', '3'], ['4', '5', '0']])

  queue.put(start)
  dist[start] = 0

  while queue.qsize()>0:
    state = queue.get()

    # We've completed the puzzle
    if state == end:
      return dist[state]

    cur_board = decode(state)
    r, c = find_zero(cur_board)
    '''
    (1). Find zero cell.
    (2). Swap with neighbors.
    '''

    for i in range(4):
      new_r, new_c = r+dr[i], c+dc[i]

      if new_r in range(R) and new_c in range(C):
        new_board = copy.deepcopy(cur_board)

        # swap with neighbors
        new_board[r][c], new_board[new_r][new_c] = new_board[new_r][new_c], new_board[r][c]

        new_state = encode(new_board)
        if new_state not in dist:
          dist[new_state] = dist[state] + 1
          queue.put(new_state)

  return -1
#-------------------------------
board = [[4,1,2],[5,0,3]]
print(solution(board))


