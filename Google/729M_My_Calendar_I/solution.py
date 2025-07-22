from sortedcontainers import SortedList

class MyCalendar:
  def __init__(self):
    self.books = SortedList([(float('-inf'), float('inf')), (float('inf'), float('inf'))])

  def book(self, start: int, end: int) -> bool:
    # look for position to possibly insert the timeslot
    # bisect_left return the leftmost index to place the timesplot in order to maintain ordered list
    # e.g [(10, 20), (30, 40)] bisect_left((15, 25)) returns 1

    # O(logN) using binary search
    position = self.books.bisect_left((start, end))
    # check if overlapping with books[position] ending time and books[position] starting time
    if start < self.books[position-1][1] or end > self.books[position][0]:
      return False

    # Log(N) to add to the sortedlist
    self.books.add((start, end))
    return True
