num_apps, num_apparts, max_diff = input().split(" ")

desired_amounts = [int(x) for x in input().split(" ")]
apartment_sizes = [int(x) for x in input().split(" ")]

desired_amounts.sort()
apartment_sizes.sort()

ans = 0
desired_pointer = 0
apartment_pointer = 0
max_diff = int(max_diff)

while desired_pointer < len(desired_amounts) and apartment_pointer < len(apartment_sizes):
    if apartment_pointer > len(apartment_sizes):
        break
    if abs(apartment_sizes[apartment_pointer] - desired_amounts[desired_pointer]) <= max_diff:
        ans += 1
        desired_pointer += 1
        apartment_pointer += 1
    else: 
        if apartment_sizes[apartment_pointer] > desired_amounts[desired_pointer]:
            desired_pointer += 1
        else:
            apartment_pointer += 1


print(ans)