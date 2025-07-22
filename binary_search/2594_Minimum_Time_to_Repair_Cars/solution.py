from math import floor, sqrt

def solution(ranks, cars):
  '''
  Observation: Binary search:
    (1). Find the value m - minutes and check if all cars can be fixed within m.
    (2). Repeat using binary search

  '''
  N = len(ranks)
  # assign all cars to highests rank mechanics
  max_time = min(ranks) * cars**2
  min_time = 1
  result = max_time

  def can_repair(m):
    '''
    Given m - minute, check if all cars can be repaired in m minutes.
    '''
    total = 0

    for rank in ranks:
      # n = sqrt(m/r)
      total += floor(sqrt(m/rank))

    return total >= cars
  #-----------------------------------
  while min_time <= max_time:
    mid = (min_time + max_time)//2

    # mid could be the result or there exists better mid on the left side
    if can_repair(mid):
      result = min(result, mid)
      max_time = mid-1

    else:
      min_time = mid+1

  return result
#-------------------------------------
ranks = [4,2,3,1]
cars = 10
print(solution(ranks, cars), ' expected: 16')
ranks = [5,1,8]
cars = 6
print(solution(ranks, cars), ' expected: 16')
