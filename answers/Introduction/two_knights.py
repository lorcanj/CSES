number = int(input())

for i in range(1, number + 1):
    # count number of ways to uniquely choose two squares on a board
    total = ((i ** 2) * ((i**2) - 1)) / 2
    # attacks occur in 2x3 block or a 3x2 block
    # only two unique attacks in each block
    # blocks don't overlap with attacks
    # count number of tiles needed to tile nxn board with overlaps
    two_by_three = (i - 2) * (i - 1)
    three_by_two = two_by_three
    attacks = (three_by_two + three_by_two) * 2
    # subtract number of attacks from total choices
    print(int(total - attacks))



