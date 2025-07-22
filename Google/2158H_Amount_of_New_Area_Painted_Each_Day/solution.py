import heapq
def solution(paint):
  '''
  Line sweeping algorithm. Illusrtation: https://leetcode.com/problems/amount-of-new-area-painted-each-day/discuss/1740812/Python-Complete-3-solutions-using-different-data-structures
  Entire idea: At day i, the job is responsible for the paint[i] that arrives earliest and still available.

  (1). We need to sort the interval but we have to make sure we remembers their original index since we need to know which one come first.
  (2). At day:
    (2.1). Grab all the paints (intervals) that has start/end date today.
    (2.2). We push its index (order of arrival) to a heap if the paint has a start date today.
    (2.3). We add its index to a set if the paint has an end date as today.
    (2.4). We then remove all the paints from the heap that has end day as today.
    (2.5). Assign the today's work for the paint that is at the top of the heap. Since this is earliest paint that arrives and still remains
           available.

  Time Complexity: O(NlogK) where K is the max value of ending time.
  '''
  records = []
  max_position = 0

  for i in range(len(paint)):
    start, end = paint[i]
    records.append((start, i, 'start'))
    records.append((end, i, 'end'))
    max_position = max(max_position, end)

  records.sort()
  # A heap that stores indices of paint that appear earliest to latest and still remained opened
  opened_work = []
  result = [0 for i in paint]
  # Store the indices of paint that already closed
  ended_work = set()
  i = 0

  for day in range(max_position+1):
    # Look for all record that has start/end date = day
    while i < len(records) and records[i][0] == day:
      pos, index, type = records[i]

      # if we encounter new paint, push its index to opened_work
      if type == 'start':
        heapq.heappush(opened_work, index)
      else:
        ended_work.add(index)

      i += 1

    # Remove all the opened_work that has ended today (starting from the earliest)
    while opened_work and opened_work[0] in ended_work:
      heapq.heappop(opened_work)

    # The opened_work[0] is responsible for today's paint since it arrives the earliest
    # In summary: today work is always be assigned for the current opened paint that arrives earliest.
    if opened_work:
      result[opened_work[0]] += 1

  return result

paint = [[1,4], [5,6], [4, 8]]
print(solution(paint))
