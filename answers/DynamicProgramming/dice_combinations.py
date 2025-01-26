n = int(input())

starter = [2 ** x for x in range(6)]
# dice has 6 sides not 5
# 1 , 2 , 4 ,8 , 16 , 32, 63 ,125, 248, 492
mod = 10 ** 9 + 7

# number of combos for each n is
# number of ways from n-r where r <= 6 and n - r > 0
# for each n-r for r in (1 - 6)
# let r = 1
# number of ways to make n-1, (we add 1 to all of those ways to make number)
# number of ways to make n-2, (we add 2 to all of those ways to make number)
# number of ways to make n-3 (we add 3 to all of those ways to make number)
# ...
# number of ways to make n - 6 (we add 6 to all of those ways to make number)
# so the answer is to build an array and then
# for n > 6
# to get n add up (n - 1) + (n - 2) ... + (n - 6)

if n <= 6:
    print(starter[n - 1])
else:
    total = sum(starter)
    subtract = 0
    for i in range(n - 6):
        starter.append((total - subtract) % mod)
        subtract += starter[i]
        total += starter[-1]
        total %= mod
    print(starter[-1])
