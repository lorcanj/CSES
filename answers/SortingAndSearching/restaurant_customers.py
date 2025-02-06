n = int(input())
starts = []
ends = []
for _ in range(n):
    pair = tuple(map(int, input().split()))
    starts.append(pair[0])
    ends.append(pair[1])

ends.sort()
starts.sort()

start_index = 0
end_index = 0
curr_ans = 0
max_ans = 0


# simply count starts and ends, adding 1 when encounter start and -1 when encounter ends
# can stop early as end will always equate to 0 due to balance or starts and ends

# while start_index < len(starts) and end_index < len(ends):
#     if curr_ans + (len(starts) - start_index) < max_ans:
#         break
#     if starts[start_index] < ends[end_index]:
#         curr_ans += 1
#         start_index += 1
#     else:
#         curr_ans -= 1
#         end_index += 1
#     max_ans = max(curr_ans, max_ans)
#
# print(max_ans)


def bin_search(starts_list, end, curr_max, minus):
    left = 0
    right = len(starts_list)

    while left < right:
        if right - minus <= curr_max:
            return -1
        # if right <+ curr_max, then can stop
        mid = left + (right - left) // 2
        # too far to the right
        if starts_list[mid] == end:
            return mid
        elif starts_list[mid] > end:
            right = mid - 1
        else:
            left = mid + 1
    return left


# for each end, count number of starts before it
# starts monotonically increasing so can binary search for that point
# subtract number of starts that finish before the current end we are looking at

minus = 0
curr_max = 0
for i in range(len(ends)):
    if (len(ends) - i) <= curr_max:
        break
    if len(starts) - minus <= curr_max:
        break

    number = bin_search(starts, ends[i], curr_max, minus)
    curr_max = max(curr_max, number - minus)
    minus += 1

print(curr_max)

# slow
# for end in ends:
#     temp = 0
#     broken = False
#     for start in starts:
#         if start[0] <= end[1]:
#             temp += 1
#         else:
#             curr_max = max(curr_max, temp - minus)
#             minus += 1
#             broken = True
#             break
#     if not broken:
#         curr_max = max(curr_max, temp - minus)


# slow
# n = int(input())
# hours = {}
#
# for _ in range(n):
#     pair = tuple(map(int, input().split()))
#     for i in range(pair[0], pair[1] + 1):
#         if i not in hours.keys():
#             hours[i] = 0
#         hours[i] += 1
#
# print(max(hours.values()))
