def solutizn(nums, queries):
  '''
  Observation: At nums[i], we count how many active intervals currently active at this point.
  Thus we use Line Sweep Algorithm:

    Initialization:
      (1). delta = [0] * (N+1)
        delta[i] how many intervals start at i

    Algorithm:
      (1). For each [L, R]:
        delta[L] += 1
        delta[R+1] -= 1

      Note that, we are += 1 at L meaning there is an interval starts at L. And this interval ends at R+1, not R.
      This delta array HASNT represented the total active intervals at any index yet. For that we must do prefix sum at the end.

      Example: queries = [1,3], [2, 4], [5,6]
                      0   1   2   3   4   5   6   7
        (1). delta = [0   0   0   0   0   0   0   0]
        (2). [1,3] = [0   1   0   0  -1   0   0   0]
            total  = [0   1   1   1   0   0   0   0] => represents total active intervals (using prefix sum on delta)

        (3). [2,4] = [0   1   1   0  -1   0  -1   0] => continue to update delta from (1)
             total = [0   1   2   2   1   1   0   0]

        (4). [5,6] = [0   1   1   0  -1   1  -1  -1] => continue to update delta from (1)
             total = [0   1   2   2   1   2   1   0] => compare this to nums at each index and we should get the result

    Time complexity: O(N+M)

  '''
  N = len(nums)
  delta = [0] * (N+1)

  for l, r in queries:
    delta[l] += 1
    delta[r+1] -= 1

  for i in range(1, N):
    delta[i] += delta[i-1]

    # early exit if total_active_intervals[i] < nums[i]
    if delta[i] < nums[i]:
      return False

  return True

nums = []
queries = []