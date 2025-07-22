def solution(arr, k, x):
  N = len(arr)
  result = []

  '''
  k closest to x

  a closer to x than b if:
  - |a-x| < |b-x|
  - |a-x| == |b-x| and a < b. Meaning a is on left side of b.

  1 2 3 4 5, k = 4, x = 3
      3
  1 2 3 4 => start at 3 (closest target to x) then expand on both side.
  '''

  '''
  Method 1: Find the closest element to x, initialize our window [L, R] there. Then expand L, R
  based on |a_L-x| and |b_R-x|.
    (1). Binary search (bisect_left to find exact location) + sliding window.
      - if x exists => good start L,R here
      - if not then compare: arr[idx-1] and arr[idx] where idx is the result of bisect_left(arr, x)
        => start L, R on which one is closer to x.
  '''

  '''
  Method 2: Search for the starting point of the window itself.
  '''
  L, R = 0, N-k # all possible starting points
  result = -1

  while L <= R:
    mid = (L+R)//2

    left_side = x - arr[mid]
    # fix edge case where arr has only 1 element
    if mid+k == N:
      # so it wont reach line 49 to get updateed.
      # we early update
      result = mid
      break
    new_right_side = arr[mid+k] - x

    '''
    Imagine it like a window of size k: [L, R] where L = mid, R = mid+k-1
    We want to check if we shift our window by 1 unit to the left: [L+1, R+1] would this be better.
    Both window overlap, however the only non-overlapping edge is: (x-a[L]) and (a[R+1]-x).
    Compare these. If (x-a[L]) > (a[R+1]-x) meaning new window [L+1, R+1] is better then we know for sure
    no window starts at L = 0 -> mid is better. And vice versa.

    For visualization: https://www.youtube.com/watch?v=o-YDQzHoaKM
    '''

    # Note: mid+k = [L, R+1]
    # compare [L, R] to [L, R+1]
    if left_side > new_right_side:
      L = mid+1
    # mid could be the best starting point
    # there could be better starting point from [0, mid-1]
    else:
      result = mid
      R = mid-1

  return arr[result:result+k]
#----------------------------------
arr = [1,2,3,4,5]
k = 4
x = 3
print(solution(arr, k, x))
arr = [1,1,2,3,4,5]
k = 4
x = -1
print(solution(arr, k, x))