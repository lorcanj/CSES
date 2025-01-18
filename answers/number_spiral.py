cached_rows = {}
cached_cols = {}
cached_twos = {}
number = int(input())
numbers = []
answer = []
for i in range(number):
    thing = input().split()

    row = int(thing[0])
    col = int(thing[1])

    ans = 0
    if row == col:
        if row not in cached_rows:
            cached_rows[row] = row ** 2
        answer.append(cached_rows[row] - (row - 1))
    elif row > col:
        # means number is on the horizontal
        if row & 1 == 0:
            if row not in cached_twos:
                cached_twos[row] = 2 ** row
            ans = cached_twos[row]
            answer.append(ans - (col - 1))
        else:
            if row not in cached_twos:
                cached_twos[row] = 2 ** row
            ans = cached_twos[row] + 1
            answer.append(ans + (col - 1))
    elif col > row:
        # is odd
        if col & 1 == 1:
            if col not in cached_cols:
                cached_cols[col] = col ** 2
            ans = cached_cols[col]
            answer.append(ans - (row - 1))
        else:
            if col - 1 not in cached_twos:
                cached_twos[col - 1] = (col - 1) ** 2
            ans = cached_twos[col - 1] + 1
            answer.append(ans + (row - 1))

for t in answer:
    print(t)



