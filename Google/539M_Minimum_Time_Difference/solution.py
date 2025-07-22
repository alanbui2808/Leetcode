def solution(time_points):
  '''
  Constraint: N = 10^4 --> O(NlogN)

  Algorithm:
  (1). Convert all the time_points to minutes in order to easily calculate between 2 points.
  (2). Sorted the time_points
  (3). Calculate the mins_diff between 2 adjacent elements.
  (4). Consider the difference between first and last points as well.
  e.g: [1:00, 17:00, 23:00] then we should also consider diff between 1:00 and 23:00 since
  it forms a cycle. We could think of the sorted list as a sorted cycle.

  Time Complexity: O(NlogN)
  '''

  # O(N)
  for i in range(len(time_points)):
    hour, mins = time_points[i].split(':')
    time_points[i] = int(hour)*60 + int(mins)

  # O(NlogN)
  time_points.sort()
  result = float('inf')

  for i in range(len(time_points)-1):
    result = min(time_points[i+1] - time_points[i], result)

  # Calculate the mins diff between first and last point because this could be another mins_diff
  # O(N)
  last_diff = time_points[-1] - time_points[0]
  result = min(result, last_diff, 24*60-last_diff)

  return result

time_points = ["1:00", "19:10", "4:45", "22:00"]
print(solution(time_points))
