number_line_length = int(input())
numbers = [int(x) for x in input().split()]

expected = (number_line_length * (number_line_length + 1))// 2
print(expected - sum(numbers))