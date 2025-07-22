def solution(candies, k):
  '''
  Observation: Binary search (maximize the minimum) and check

  '''
  N = len(candies)

  def enough_candies(m):
    '''
    Given m - candies, check if we have at least k piles where each pile has >= m candies.
    '''
    total = 0

    for i in range(N):
      total += candies[i]//m

    return total>=k
  #--------------------------
  L = 1
  R = sum(candies)//k
  res = 0

  while L <= R:
    mid = (L+R)//2

    if enough_candies(mid):
      res = mid
      L = mid+1
    else:
      R = mid-1

  return res
#-----------------------------------
candies = [5,8,6]
k = 3
print(solution(candies, k), ' expected: 5')
candies = [2,5]
k = 11
print(solution(candies, k), ' expected: 0')
candies = [4,7,5]
k = 4
print(solution(candies, k), ' expected: 3')

