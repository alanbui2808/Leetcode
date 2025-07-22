def solution(matrix):
  '''
  Observation:
  At each point (r, c) we need to determine all possible directions that we could form a longest line and take the max among them
  We can quickly compute this if we know the longest lines of all the directions for the children cells.

  Algorithm:
  (1). dp[r][c] = (ll_left+1, ll_diag+1, ll_top+1, ll_antidiag+1)
  (2). result = max(result, max(dp[r][c]))


  Time complexity: O(MN)
  Space: O(4MN)
  '''
  M, N = len(matrix), len(matrix[0])

  # dp[i][j] = (longest_line from the left + mat[i][j], longest_line from the diagonal, ll from the top, ll from the anti-diag)
  dp = [[(0,0,0,0) for c in range(N)] for r in range(M)]
  result = 0

  for r in range(M):
    for c in range(N):
      if matrix[r][c] == 0:
        continue

      # Longest line we could form from the left
      ll_left = dp[r][c-1][0] if c-1 in range(N) and matrix[r][c-1] == 1 else 0
      # Longest line we could form from the diagonal
      ll_diag = dp[r-1][c-1][1] if r-1 in range(M) and c-1 in range(N) and matrix[r-1][c-1] == 1 else 0
      # Longest line we could form from the top
      ll_top = dp[r-1][c][2] if r-1 in range(M) and matrix[r-1][c] == 1 else 0
      # Longest line we could form from the anti-diagonal
      ll_antidiag = dp[r-1][c+1][3] if r-1 in range(M) and c+1 in range(N) and matrix[r-1][c+1] == 1 else 0

      # Update for dp[r][c] from all directions that we could form a longest
      dp[r][c] = (ll_left+1, ll_diag+1, ll_top+1, ll_antidiag+1)

      result = max(max(dp[r][c]), result)

  return result
#----------------------------------------------------------
matrix = [[1,1,1,1],[0,1,1,0],[0,0,0,1]]
print(solution(matrix))
