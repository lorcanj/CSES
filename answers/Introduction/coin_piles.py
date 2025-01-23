number = int(input())

for i in range(number):
    values = [int(x) for x in input().split()]
    a = max(values)
    b = min(values)
    iterations = a - b
    if b - iterations < 0:
        print("NO")
    else:
        new_a = a - 2*iterations
        new_b = b - iterations
        if new_a % 3 == 0:
            print("YES")
        else:
            print("NO")

# logic, assume a > b
# if a always > b, then false
# when?
# let t be number of iterations
# numbers are equal when line below is correct and evaluated
# a-2t = b - t
# a - b = 2t - t
# a - b = t
# so can find t