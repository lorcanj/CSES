# naive recursive solution
# def get_subset(target, current_array: list, choices):
#     if target == 0:
#         return True, current_array.copy()
#     if target < 0:
#         return False, []
#     for i in range(choices - 1, -1, -1):
#         without_choice = get_subset(target, current_array, choices - 1)
#         current_array.append(choices)
#         with_choice = get_subset(target - choices, current_array, choices - 1)
#         current_array.pop()
#         if with_choice and with_choice[0]:
#             return True, with_choice[1]
#         if without_choice and without_choice[0]:
#             return True, without_choice[1]

# iterative naive solution
# def get_subset(target, choices):
#     # current array and current_sum
#     stack = [([choices], choices)]
#     while stack:
#         choices -= 1
#         length = len(stack)
#         for i in range(length):
#             things = stack[i]
#             if choices == 0:
#                 break
#             if things[1] + choices <= target:
#                 if things[1] + choices == target:
#                     things[0].append(choices)
#                     return things[0]
#
#                 c = things[0].copy()
#                 c.append(choices)
#                 stack.append((c, things[1] + choices))
#         curr = stack.pop()
#         new = curr[0].copy()
#         stack.append((new, curr[1]))
#         if curr[1] == target:
#             return curr[0]

import math


def get_subsets(number):
    answer_one = []
    answer_two = []
    pos_neg = 1
    if number % 4 == 0:
        n = number + 1
        for i in range(1, math.ceil((number + 1) / 2)):
            if pos_neg > 0:
                answer_one.append(i)
                answer_one.append(n - i)
                pos_neg *= -1
            else:
                answer_two.append(i)
                answer_two.append(n - i)
                pos_neg *= -1
    else:
        n = number + 1
        # 4 5 6 7 8 9 10 11
        for i in range(1, ((n - 3) // 2) + 1):
            if pos_neg > 0:
                answer_one.append(i + 3)
                answer_one.append(n - i)
                pos_neg *= -1
            else:
                answer_two.append(i + 3)
                answer_two.append(n - i)
                pos_neg *= -1
        answer_one.append(1)
        answer_one.append(2)
        answer_two.append(3)
    return answer_one, answer_two


number = int(input())
sum_one_to_n = (number * (number + 1)) // 2
if sum_one_to_n & 1 == 1:
    print("NO")
else:
    # know the amount can be generated
    # subsets can be generated if number % 4 == 0 or 3
    # set_other_numbers = {i for i in range(1, number + 1)}
    # other_numbers = list(set_other_numbers - set(ans))
    ans = get_subsets(number)
    print("YES")
    print(len(ans[0]))
    for i in ans[0]:
        print(f"{i} ", end='')
    print("")
    print(len(ans[1]))
    for i in ans[1]:
        print(f"{i} ", end='')
