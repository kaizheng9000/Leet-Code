from collections import defaultdict
import heapq


def highFive(items):
        """
        :type items: List[List[int]]
        :rtype: List[List[int]]
        """

        scores = defaultdict(list)
        result = []

        for studentId, score in items:
            heapq.heappush(scores[studentId], score)
            if len(scores[studentId]) > 5:
                  heapq.heappop(scores[studentId])

        for studentId, score in dict(sorted(scores.items())).items():
            avg = sum(score) / 5
            result.append([studentId, avg])

        return result



print(highFive([[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]))