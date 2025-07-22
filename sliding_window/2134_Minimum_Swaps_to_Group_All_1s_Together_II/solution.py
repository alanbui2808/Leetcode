def solution(nums):
  '''
  Observation:
    (1). Circular array, we append same nums to the end. However we can determine exactly how many
    elements are needed instead of all.

    (2). Notice: We need to find a window [L, R]:
    - size total 1s
    - where # of 0s is the smallest.

    Thus this denotes how many swaps we need. Thus the max_swaps we need is total 1s-1.
    Therefore we need to append only max_swaps number of elements to the end.

    E.g: [1 ... 0][max_swaps], Suppose any idx can be the start of [L, R] then the last idx would
    be N-1, thus L = N-1, and we need a window of size of total 1s, thus max_swaps elements.

    any window starts at L = N basically repeats the same process (circular)

  Algorithm:
    (1). Start with window of fixed size [L, R] where size = total 1s.
    (2). Records 0s, update result each time.
    (3). Increment L and R.
  Time: O(N)

  '''
  N = len(nums)
  ones = sum(nums)

  if ones == 0: return 0

  max_swaps = ones-1
  L = 0
  zeros = 0
  result = max_swaps

  # start with [L, max_swap-1] and collect 0s
  for R in range(max_swaps):
    zeros += nums[R]==0

  for R in range(max_swaps, N+max_swaps):
    # Check 0s inside [L, R]
    zeros += nums[R%N]==0 # could be out of range
    result = min(result, zeros)

    # shrink L and update 0s
    zeros -= nums[L%N]==0
    L += 1


  return result
#----------------------------
nums = [0,1,0,1,1,0,0]
print(solution(nums), ' expected: 1')
nums = [0,1,1,1,0,0,1,1,0]
print(solution(nums), ' expected: 2')
nums = [1,1,0,0,1]
print(solution(nums), ' expected: 0')




