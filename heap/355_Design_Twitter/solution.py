from collections import defaultdict
from heapq import heapify, heappop, heappush

class Twitter:
  '''
  Observation: Similar to merge k sorted array.
    (1). Assume we have:
      - tweets:   a dict of (userId: list of (time, tweetId))
      - follows:  a dict of (userId: set of followeeId)

    (2). To get 10 most recent posts among all followee and themselve, at each iteration they need to find:
      - (time, tweetId) with largest time among all followees and themselve.

      For example: Let's say user 1 has followee and their tweets as:
        user        (time, tweetId)
        1          (1,2) (3,4) (5,1)
        2          (2,3) (4,7)
        3          (6,6) (7,5)

      Then at iteration we need to compare between (1,2), (2,3) and (6,6) => we need to use min_heap. This is exactly as
      merging k sorted list.

      - The only difference that, after we pop an entry out of max_heap, we need to know the next element. Thus we need an entry
      as: (time, tweetId, followeeId, idx).
      - From this, we will know what followeeId to look for their tweets and idx will indicate the next tweet available.

  Time: O(10logK + K) => O(K) for heapify and 10logK for 10 iterations of pop/push 10 most recent posts.
  Space: O(K + KT + max(10, K))
    - O(K) for follows
    - O(KT) for tweets
    - O(max(10, k)) for max_heap


  '''
  def __init__(self):
    self.time = -1
    self.tweets = defaultdict(list)   # userId -> list of (time, tweetId)
    self.follows = defaultdict(set)   # userId -> set of followeeId

  def postTweet(self, userId: int, tweetId: int) -> None:
    self.tweets[userId].append((self.time, tweetId))

    self.time -= 1

  def getNewsFeed(self, userId: int) -> List[int]:
    res = []
    max_heap = []
    k = 0
    # Need to include tweets of themselves
    if userId not in self.follows[userId]:
      self.follows[userId].add(userId)

    for followeeId in self.follows[userId]:
      # get no of tweets of this followee
      idx = len(self.tweets[followeeId])-1

      if idx>=0:
        # grab most recent tweet
        time, tweetId = self.tweets[followeeId][idx]

      max_heap.append((time, tweetId, followeeId, idx))

    heapify(max_heap)

    while max_heap and k<10:
      time, tweetId, followeeId, idx = heappop(max_heap)
      res.append(tweetId)

      if idx-1>=0:
        # grab the next most recent tweet from followeeId
        time, tweetId = self.tweets[followeeId][idx-1]
        heappush(max_heap, (time, tweetId, followeeId, idx-1))

      k += 1

    return res

  def follow(self, followerId: int, followeeId: int) -> None:
    self.follows[followerId].add(followeeId)

  def unfollow(self, followerId: int, followeeId: int) -> None:
    if followeeId in self.follows[followerId]:
      self.follows[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)