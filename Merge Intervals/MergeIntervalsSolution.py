
example = [[1,3],[2,6],[8,10],[15,18]]
example2 = [[1,4],[4,5]]

def merge_intervals(intervals):

    if len(intervals) == 1:
        return intervals

    result = []
    sorted_list = sorted(intervals)
    lower = sorted_list[0][0]
    upper = sorted_list[0][1]
    current = []

    for i in range(1, len(sorted_list)):
        if sorted_list[i][0] <= upper:
            # max_upper = ma
            current = [lower, sorted_list[i][1]]
            result.append(current)
            lower = sorted_list[i][0]
            upper = sorted_list[i][1]
        else:
            if i == 1:
                result.append(sorted_list[0])
            result.append(sorted_list[i])
    return result

print(merge_intervals(example))