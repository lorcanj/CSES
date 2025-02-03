n = int(input())
numbers = [int(x) for x in input().split()]


def rec_count(a, b, counter, inputty):
    if counter == len(inputty):
        return abs(a - b)
    left = rec_count(a + inputty[counter], b, counter + 1, inputty)
    right = rec_count(a, b + inputty[counter], counter + 1, inputty)

    return min(left, right)


print(rec_count(0, 0, 0, numbers))
