def solution(grid):
  '''
  Observation:
  Let's say there are some number of 1s in the first row.
  To get to all 0s matrix it is obvious that we must flip those 1s.
  If we flip the first row itself then any 0 will turn into 1.
  So instead, we flip all the columns that have 1 in the first row.
  Now if we think a little deeply, we can realize that we can never flip columns again, because if we do, then 0s in first row will turn to 1s again.
  So our only option is to flip rows now (starting from second row since first row is already all 0s).
  Now to get all 0s in the final matrix each row ought to have either only 0s or only 1s. If it has only 0s we don't flip it, if it has only 1s then we flip it. If in any row all the elements are not same, it means it is not possible to get all 0s matrix.

  Time Complexity: O(MN)
  '''
  M, N = len(grid), len(grid[0])

  for c in range(N):
    if grid[0][c] == 1:
      for r in range(M):
        grid[r][c] = 1 - grid[r][c] # 1 -> 0 and 0 -> 1

  for r in range(M):
    for c in range(1, N):
      if grid[r][c] != grid[r][c-1]:
        return False

  return True

#------------------------------------
grid = [[0]]
print(solution(grid))
