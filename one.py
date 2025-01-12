number = int(input())
temp = []
while number != 1:
    temp.append(str(number) + " ")
    # could check for a perfect square
    if number & 1 == 0:
        number //= 2
    else:
        number = (number * 3) + 1

temp.append(str(number))
print(''.join(temp))