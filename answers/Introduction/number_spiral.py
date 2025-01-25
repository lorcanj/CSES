n = int(input())

for _ in range(n):
    row, col = map(int, input().split())
    row -= 1
    col -= 1
    m = max(row, col)
    if m == 0:
        print(1)
    else:
        # can tell if moving down or up depending on whether pre
        previous_layer = m * m
        # odd
        if previous_layer & 1 == 1:
            # current is even so moving downwards
            if col > row:
                print(previous_layer + row + 1)
            else:
                print(previous_layer + row + (m - col) + 1)
        else:
            # current is odd so moving upwards
            if row > col:
                print(previous_layer + col + 1)
            else:
                print(previous_layer + col + (m - row) + 1)
