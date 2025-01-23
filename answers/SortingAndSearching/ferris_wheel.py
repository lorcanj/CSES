n, x = input().split(" ")
weights = [int(x) for x in input().split(" ")]

weights.sort()

left = 0
right = len(weights) - 1
ans = 0
x = int(x)

while left <= right:
    if left == right:
        ans += 1
        break
    if weights[right] + weights[left] > x:
        right -= 1
        ans += 1
    else:
        right -= 1
        left += 1
        ans += 1

print(ans)