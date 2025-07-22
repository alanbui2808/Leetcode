from collections import defaultdict

def solution(nums):
  N = len(nums)

  '''
  Sliding Window + Count

  Observation:
    (1). Given [L, R] that is completed => all subarrays [L, R+1], ... [L, N-1] is also completed.
    => we have total: N-R completed subarrays given [L, R]

  Algorithm:
    (1). Sliding window: [L, R] until it's completed.
    (2). Record result
    (3). Shrink L until [L, R] is no longer completed.

  Time: O(N)
  Space: O(9)
  '''

  dist = set(nums)
  dist_sub = defaultdict(int)
  L = 0
  result = 0

  for R in range(N):
    dist_sub[nums[R]] += 1

    while L <= R and len(dist) == len(dist_sub):
      result += N-R

      # shrink until [L, R] has less than total distinct elements
      dist_sub[nums[L]] -= 1
      if dist_sub[nums[L]] == 0:
        del dist_sub[nums[L]]

      L += 1

  return result

#-----------------------------------------
nums = [1,3,1,2,2]
print(solution(nums), ' expected: 4')
nums = [5,5,5,5]
print(solution(nums), ' expected: 10')



