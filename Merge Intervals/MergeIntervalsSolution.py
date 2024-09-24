
example = [[1,3],[2,6],[8,10],[15,18]]
example2 = [[1,4],[4,5]]
example3 = [[1,4],[2,3]]

def merge_intervals(intervals):

    if len(intervals) == 1:
        return intervals

    result = []
    sorted_list = sorted(intervals)

    for interval in sorted_list:
        if not result or result[-1][1] < interval[0]: # Check for overlap
            result.append(interval)
        else:   # Need to merge
            result[-1] = [result[-1][0], max(result[-1][1], interval[1])]

    return result


print(merge_intervals(example))