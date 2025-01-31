t = int(input())
#
numbers = [int(x) for x in input().split()]
# t = 5
#
# numbers = [1, 1, 2, 3]

# what should the right output be
# want the count of direct reports
# 1 := 2
# 2 := 1
# 3 := 1
# 4 := 0
# 5 := 0

hierarchy = {}
for i in range(1, t + 1):
    hierarchy[i] = []

for i in range(1, len(numbers) + 1):
    hierarchy[numbers[i - 1]].append(i + 1)

cache = {}

# want to do this with a stack rather than recursion to stop the recursive errors
def count_things(dictionary, number):
    if len(dictionary[number]) == 0:
        cache[number] = 0
        return 0
    if number in cache:
        return cache[number]

    total = len(dictionary[number])
    for num in dictionary[number]:
        if num in cache:
            total += cache[num]
        else:
            total += count_things(dictionary, num)

    cache[number] = total
    return total


for k, v in hierarchy.items():
    count_things(hierarchy, k)

for i in range(1, t+1):
    print(cache[i], end=' ')
