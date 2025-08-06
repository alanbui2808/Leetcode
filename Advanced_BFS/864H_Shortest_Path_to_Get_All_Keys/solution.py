from queue import Queue
import copy

def solution(grid):
  '''
  Observation:
    (1). We can traverse to the same cell in the grid multiple times. However each time we traverse we might or might not have the same
    number of keys.
    (2). Thus we BFS on state = (r, c, list_of_keys we collected so far). Thus we can visit (r,c) multiple times but only if we have
    a new collected list_of_keys.

  Algorithm:
    (1). Define a state as following: (r, c, [T, F, T, F, T, F]) where 'T' means we have collected this key, otherwise not.
    (2). Run BFS on this 'graph' of state.
    (3). At each state:
      (3.1). We only consider neighbors that are not a wall.
      (3.2). If it's an empty or goal or a lock (but we have a key to unlock it from parent state) -> we can visit, however list_of_keys
      does not change.
      (3.3). If it's a key and we've not collected it. We update list_of_keys to collect it.
      (3.4). Ignore if it's a lock and we cannot unlock.
      (3.5). new_state = (new_r, new_c, new_list_of_keys). Check if visited or not and then put it to queue and continue to explore respectively.

    Note: Since this problem, the state is complicated and unhashable by Python dict. Thus we convert it into a string.

  Time: O(V + E). V (number of states) = MN * 2^6, E = 4 * V. Thus O(MN * 2^6)
  Space: O(V)
  '''
  # state = (r, c, [T,F, ..., F])
  keys = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5}
  R, C = len(grid), len(grid[0])

  def encode(r: int, c: int, cur_keys: list[str]) -> str:
    '''
    Given (r:int, c:int, keys - [T, F, .., T]:list[str]), convert it to string: 'r,c,TFTFTF'
    '''
    coordinate = str(r) + ',' + str(c)
    cur_keys = ''.join(cur_keys)

    return coordinate + ',' + cur_keys

  def decode(value: str) -> tuple[int, int, list[str]]:
    '''
    Given a string 'r,c,TTFFTF', convert it to (r:int, c:int, keys - [T, F, ..., T]: list[str])
    '''
    r, c, keys = value.split(',')
    r, c, keys = int(r), int(c), list(keys)

    return r, c, keys

  def is_key(cell):
    return cell != '.' and cell != '@' and cell.islower()
  def is_lock(cell):
    return cell != '.' and cell != '@' and cell.isupper()

  queue = Queue()
  dr = [1, -1, 0, 0]
  dc = [0, 0, -1, 1]
  dist = {}
  total_keys = 0

  for r in range(R):
    for c in range(C):
      if grid[r][c] == '@':
        cur_keys = ['F' for k in range(6)]
        state = encode(r, c, cur_keys)

        dist[state] = 0
        queue.put(state)

      elif is_key(grid[r][c]):
        total_keys += 1

  while queue.qsize()>0:
    state = queue.get()
    r, c, cur_keys = decode(state)

    # Check if we have collected all the keys
    collected = 0
    for key in cur_keys:
      if key == 'T':
        collected += 1

      if collected == total_keys:
        return dist[state]

    for i in range(4):
      new_r, new_c = r+dr[i], c+dc[i]

      if new_r in range(R) and new_c in range(C) and grid[new_r][new_c] != '#':
        cell = grid[new_r][new_c]

        new_keys = copy.deepcopy(cur_keys)

        # (1). empty or goal cell
        # (2). lock
        # (3). key

        # a lock and we dont have a key to unlock it
        if is_lock(cell) and new_keys[keys[cell.lower()]] == 'F':
          continue

        # a new key that has not been collected
        if is_key(cell) and new_keys[keys[cell]] == 'F':
            new_keys[keys[cell]] = 'T'

        # a lock (with a key to unlock) or empty or goal cell will have the same number of keys as the previous state
        new_state = encode(new_r, new_c, new_keys)

        if new_state not in dist:
          dist[new_state] = dist[state] + 1
          queue.put(new_state)

  return -1

#------------------------------------------
grid = ["@Aa"]
print(solution(grid))










