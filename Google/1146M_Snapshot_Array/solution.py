from collections import defaultdict

class SnapshotArray:
  '''
  We store a list:
  0:  (snap_id, value)
  1:
  2:
  .
  n:

  Thus there is case where:
  0: (0,0) (1,5) (2,6) (3,7)
  1: (0,0) (1,2) (3,6) --> this is because we didn't set anything for index 1 during snap_id = 2
  2: (0,0) --> when we call get(2, snap_id=2) -> we return 0

  To quickly look for snap_id in list[index], we use binary search. However we are looking for largest snap_id <= target_snap_id (we see get(2, snap_id=2) = 0)

  To quickly understand the binary below (where we use <= instead <), consider the example: [0,1 ,3] and target = 2
  '''
  def __init__(self, legnth: int):
    self.map = {i: [[0, 0]] for i in range(length)}
    self.snap_id = 0

  def set(self, index: int, val: int) -> None:
    if self.map[index][-1][0] == snap_id:
      # override if the top element is currently at snap_id
      self.map[index][-1][1] = val
    else:
      self.map[index].append([snap_id, val])

  def snap(self) --> int:
    self.snap_id += 1
    return self.snap_id - 1

  def get(self, index: int, snap_id: int) -> int:
    # we are looking for largest val <= snap_id
    arr = self.snap[index]

    L, R = 0, len(arr) - 1
    # default should be 0
    ans = 0

    while left <= right:
      # Since we continuely looking for value <= snap_id, we must continue
      # shrink our window until there is nothing left, i.e left > right
      # then it is guarantee that the answer we store is the largest value <= snap_id
      mid = (left+right) // 2

      if arr[mid][0] == snap_id:
        ans = mid
        break

      elif arr[mid][0] < snap_id:
        # this could be a solution since we are looking for val <= snap_id so we store this
        ans = mid
        # We can ignore this value and shrink our window size
        L = mid + 1

      else:
        # We completely ignore this value
        R = mid - 1

    return arr[ans][1]

