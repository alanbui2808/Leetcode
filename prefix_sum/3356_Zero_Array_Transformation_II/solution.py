def solution(nums, queries):
  '''
  Observation:
    (1). Line+sweep + BS: O((N+M)*logM))
    (2). Pure linesweep: O(N+M)
  '''
  N = len(nums)
  M = len(queries)
  if sums(nums) == 0: return 0
  result = M+1


  def is_zero_array(k):
    delta = [0]*(N+1)

    for i in range(k+1):
      l, r, v = queries[i]
      delta[l] += v
      delta[r+1] -= v

    for i in range(N):
      delta[i] += delta[i-1] if i-1>=0 else 0

      if delta[i] < nums[i]:
        return False

    return True
  #------------------------------------
  L, R = 0, M-1

  while L<=R:
    k = L + (R-L)//2

    if is_zero_array(k):
      result = min(result, k+1)
      # shrink [L, k-1]
      R = k-1
    else: # expand [k+1, R]
      L = k+1

  return result if result < M+1 else -1

nums = [4,3,2,1]
queries = [[1,3,2],[0,2,1]]
print(solution(nums, queries))
