length = int(input())
numbers = [int(x) for x in input().split()]

ans = 0
for i in range(length - 1):
    change = max(0, numbers[i] - numbers[i + 1])
    ans += change
    numbers[i + 1] += change
print(ans)
