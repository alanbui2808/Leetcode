from bisect import bisect_left, bisect_right
# from math import ceil
def solution(nums1, nums2, k):
  '''
  Observation:
    (1). Use binary search to find a val and check if val is >= k elements.
    (2). To count how many (x,y) s.t x * y <= val. We can fix x, and count how many y <= val/x also using binary search.
      Note: x * y <= val then:
      - if x > 0: y <= val / x
      - if x < 0: y >= val/x (inequality flips)
      - if x = 0: y can be anything as long as val >= 0.


  Algorithm:
    (1). Use binary search on range [L = -10**10-1, R = 10**10+1].
    (2). For each mid, count(mid).
    (3). count(mid):
      - For each x in nums1, use binary search to how many y <= val/x, y >= val/x, etc depends on the sign of x.

    (4). Shrink L, R accordingly.

  Time:
    (1). O(logR * NlogM) where R - search space, N = len(nums1) and M = len(nums2)

  Space: O(1)
  '''
  N, M = len(nums1), len(nums2)

  def count(val):
    '''
    Given val, count how many x * y <= val by pairing (x, y) in n1 and n2
    '''
    cnt = 0

    # x*y <= val
    for x in nums1:
      # y <= val/x
      if x > 0:
        cnt += bisect_right(nums2, val/x)

      # y >= val/x (inequality flips)
      if x < 0:
        cnt += M - bisect_left(nums2, val/x)

      # x = 0 thus x*y == 0
      if x == 0 and val >= 0: # only count if val >= 0
        cnt += M

    return cnt
  #-------------------------------------
  L, R = -10**10 - 1, 10**10 + 1
  res = R

  while L <= R:
    mid = (L+R)//2

    # if mid is greater >= k elements
    if count(mid) >= k:
      res = mid
      R = mid-1 # explore the lower half
    else:
      L = mid+1

  return res
#------------------------
nums1 = [2,5]
nums2 = [3,4]
k = 2
print(solution(nums1, nums2, k), ' expected: 8')
nums1 = [-4,-2,0, 3]
nums2 = [2,4]
k = 6
print(solution(nums1, nums2, k), ' expected: 0')
nums1 = [-2,-1,0,1,2]
nums2 = [-3,-1,2,4,5]
k = 3
print(solution(nums1, nums2, k), ' expected: -6')
nums1 = [-6]
nums2 = [-9]
k = 1
print(solution(nums1, nums2, k), ' expected: 10')

