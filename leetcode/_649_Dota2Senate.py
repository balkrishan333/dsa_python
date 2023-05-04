import collections


class Solution:

    def predictPartyVictory(self, senate: str) -> str:
        rqueue = collections.deque()
        dqueue = collections.deque()

        for index, char in enumerate(senate):
            if char == 'R':
                rqueue.append(index)
            else:
                dqueue.append(index)

        while rqueue and dqueue:
            rindex = rqueue.popleft()
            dindex = dqueue.popleft()

            if rindex < dindex:
                newEle = rindex + len(senate)
                rqueue.append(newEle)
            else:
                newEle = dindex + len(senate)
                dqueue.append(newEle)

        if rqueue:
            return "Radiant"
        return "Dire"


sln = Solution()
print(sln.predictPartyVictory("RDD"))
