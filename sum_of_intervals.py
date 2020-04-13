# def sum_of_intervals(intervals):
#     intervals = [list(i) for i in intervals]
#     intervals.sort(key=lambda x: x[0])
#     for j in range(len(intervals) - 1):
#         for i in range(len(intervals) - 1):
#             if intervals[i][1] in range(intervals[i + 1][0], intervals[i + 1][1]):
#                 intervals[i][1] = intervals[i + 1][1]
#             elif intervals[i + 1][1] in range(intervals[i][0], intervals[i][1]):
#                 intervals[i + 1][1] = intervals[i][1]
#     for i in range(len(intervals) - 1):
#         if intervals[i][1] == intervals[i + 1][1]:
#             intervals[i + 1][0] = intervals[i][0]
#     result = []
#     for i in intervals:
#         if i not in result:
#             result.append(i)
#     return sum([i[1] - i[0] for i in result])


l = [(1, 2), (6, 10), (11, 15)]
l = [[1,4],
   [7, 10],
   [3, 5]]
# print(sum_of_intervals(l))
def sum_of_intervals(intervals):
    result = set()
    for start, stop in intervals:
        for x in range(start, stop):
            result.add(x)
    return len(result)
        # print(start, stop)

print(sum_of_intervals(l))

