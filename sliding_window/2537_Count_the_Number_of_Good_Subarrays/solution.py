from collections import defaultdict

def solution(nums, k):
  '''
  Observation: Sliding window.
    (1). Given [L, R] with pairs >= k, then all subarrays ending at [L, R], [L, R+1], ... [L, N-1]
    are included. Thus the total # subarrays = N-R
    (2). Shrink L and repeat until pairs < k.

  Time: O(N)
  '''
  N = len(nums)
  count = defaultdict(int)
  pairs = 0
  result = 0
  L = 0

  for R in range(N):
    # there are count[nums[R]] before this nums[R], therefore the total new pairs
    # that can form with nums[R] is count[nums[R]]
    # e.g [2 2] 2 => count[2] = 2 => 2 new pairs are formed.
    pairs += count[nums[R]]
    count[nums[R]] += 1

    while pairs >= k:
      # all subarrays ending at [L: R...N] are included.
      result += N-R

      # shrink [L, R]
      # similar reasoning to total of new pairs formed when adding 1 more element but reverse
      # e.g: [2 2 2] => 2 [2 2] => count[2] = 2 => 2 pairs are disjointed
      count[nums[L]] -= 1
      pairs -= count[nums[L]]
      L += 1

  return result




nums = [1,1,1,1,1]
k = 1
print(solution(nums, k))
nums = [3,1,4,3,2,2,4]
k = 2
print(solution(nums, k))
nums = [1,2,2,2]
k = 2
print(solution(nums, k))
