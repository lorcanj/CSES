number = int(input())
ans = []
can_compute = True
if number > 1 and number < 4:
    can_compute = False
else:
    # output depends on length being odd or even
    # even
    if number & 1 == 0:
        for i in range(number - 1, 0, -2):
            ans.append(f"{str(i)} ")

        for i in range(number, 1, -2):
            ans.append(f"{str(i)} ")
    # odd
    else:
        for i in range(number - 2, 0, -2):
            ans.append(f"{str(i)} ")

        ans.append(f"{str(number)} ")

        for i in range(2, number, 2):
            ans.append(f"{str(i)} ")

if can_compute:
    answer = ''.join(ans).strip()
    print(answer)
else:
    print("NO SOLUTION")






