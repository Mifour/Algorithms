class Solution:
  def minMeetingRooms(self, intervals):
    start = []
    end = []
    for i in intervals:
      start.append(i[0])
      end.append(i[1])
    start.sort()
    end.sort()

    s = 0
    e = 0
    numRooms = 0
    available = 0

    while s < len(start):
      if start[s] < end[e]:
        if available:
          available -= 1
        else:
          numRooms += 1
        s += 1
      else:
        available += 1
        e += 1
    return numRooms

