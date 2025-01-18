cached_rows = {}
cached_cols = {}
cached_twos = {}

n = int(input())

for _ in range(n):
    row, col = map(int, input().split())

    ans = 0
    if row == col:
        if row not in cached_rows:
            cached_rows[row] = row ** 2
        print(cached_rows[row] - (row - 1))
    elif row > col:
        # means number is on the horizontal
        if row & 1 == 0:
            if row not in cached_twos:
                cached_twos[row] = 2 ** row
            print(cached_twos[row] - (col - 1))
        else:
            if row not in cached_twos:
                cached_twos[row] = 2 ** row
            print(cached_twos[row] + 1 + (col - 1))
    elif col > row:
        # is odd
        if col & 1 == 1:
            if col not in cached_cols:
                cached_cols[col] = col ** 2
            print(cached_cols[col] - (row - 1))
        else:
            if col - 1 not in cached_twos:
                cached_twos[col - 1] = (col - 1) ** 2
            print(cached_twos[col - 1] + 1 + (row - 1))




