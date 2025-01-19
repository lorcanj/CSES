exponent = int(input())
if exponent == 0:
    print(1)
else:

    mod = 10**9 + 7
    ans = 2
    for _ in range(exponent - 1):
        ans *= 2
        ans = ans % mod
    print(ans)



