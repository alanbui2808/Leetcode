class StockPrice:
  '''
  (1). We need hashmap to quickly update the price for timestamp.
  (2). To quickly return max and min as well as constructing the max, min we need max_heap and min_heap

  Time Complexity: O(NlogN) where N is the number of calls, this means all the operation should be <= O(logN)
  '''
  def __init__(self):
    self.latest_time = 0
    # Store price of each stock at each timestamp.
    self.timestamp_price_map = {}

    # Store stock prices in sorted order to get min and max price.
    self.max_heap = []
    self.min_heap = []

  def update(self, timestamp: int, price: int) -> None:
    # Update latestTime to latest timestamp.
    self.timestamp_price_map[timestamp] = price
    self.latest_time = max(self.latest_time, timestamp)

    # Add latest price for timestamp.
    # O(log(N))
    heappush(self.min_heap, (price, timestamp))
    heappush(self.max_heap, (-price, timestamp))

  def current(self) -> int:
    # Return latest price of the stock.
    return self.timestamp_price_map[self.latest_time]

  def maximum(self) -> int:
    price, timestamp = self.max_heap[0]

    # Key point:
    # Pop all pairs from the heap where the price does not match with the price in the hash
    # O(log N)
    while -price != self.timestamp_price_map[timestamp]:
      heappop(self.max_heap)
      price, timestamp = self.max_heap[0]

    return -price

  def minimum(self) -> int:
    price, timestamp = self.min_heap[0]

    # Pop all pairs from the heap where the price does not match with the price in the hash
    # O(log N)
    while price != self.timestamp_price_map[timestamp]:
      heappop(self.min_heap)
      price, timestamp = self.min_heap[0]

    return price