from collections import defaultdict

def solution(nums, k):
  '''
  Observation:  Sliding Window + maintain a fixed size window

  '''
  N = len(nums)
  cnt = defaultdict(int)
  total = 0
  L = 0
  result = 0

  for R in range(N):
    cnt[nums[R]] += 1
    total += nums[R]

    # Shrink until [L, R] can include nums[R] and size <= k
    while L < R and (cnt[nums[R]] > 1 or R-L+1 > k):
      cnt[nums[L]] -= 1
      total -= nums[L]
      L += 1

    # [L, R] is valid and len([L,R]) <= k
    if R-L+1 == k:
      result = max(result, total)

  return result


nums = [1,5,4,2,9,9,9]
k = 3
print(solution(nums, k), ' expected: 15')
nums = [4,4,4]
k = 3
print(solution(nums, k), ' expected: 0')
