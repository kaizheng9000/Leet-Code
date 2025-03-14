def highFive(self, items):
        """
        :type items: List[List[int]]
        :rtype: List[List[int]]
        """

        scores = {}
        result = []

        for student, score in items:
            if student not in scores:
                scores[student] = [score]
            else:
                scores[student].append(score)

        for key, value in scores.items():
            scores[key] = sorted(value, reverse=True)
            avg = sum(scores[key][:5]) / 5
            result.append([key, avg])

        sorted(result)

        return result