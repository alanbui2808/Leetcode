def solution(nums, target):
  '''
  Sliding window, [L, R] until >= target, then shrink until < target then repeat.
  '''
  N = len(nums)
  L = 0
  R = -1
  # start with window ][ (will see why later when shrinking)
  cur_sum = 0
  result = N+1

  for R in range(N):
    # standard implementation
    cur_sum += nums[R]

    if cur_sum >= target:
      # shrink [L, R] until cur_sum < target
      # There could be a case where we must shrink all the elements out of [L, R]
      for L in range(L, R+1): # thus explains the range of L = [L, R+1]
        if cur_sum < target:
          break

        result = min(result, R-L+1)

        # shrink [L, R]
        cur_sum -= nums[L]
        L += 1

      # 2 cases after the shrink: L <= R, L = R+1
      # L <= R: [L, R] has cur_sum < target
      # L > R:  R][L means pops out all elements to make cur_sum < target. E.g: [1,10] target = 10

  return result if result < N+1 else 0
#---------------------------------
nums = [2,3,1,2,4,3]
target = 7
print(solution(nums, target))
nums = [1,4,4]
target = 4
print(solution(nums, target))
nums = [1,1,1,1,1,1,1,1]
target = 11
print(solution(nums, target))
