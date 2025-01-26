pali = input()

letters = {}
for l in pali:
    if l not in letters:
        letters[l] = 0
    letters[l] += 1


def check_valid(d_letters: dict):
    odd = False

    for k, v in d_letters.items():
        if v & 1 == 1:
            if odd:
                return False, odd
            odd = True
    return True, odd


values = check_valid(letters)
if not values[0]:
    print("NO SOLUTION")
else:
    odd = values[1]
    ans = [None] * sum(v for v in letters.values())

    start = 0
    end = len(ans)
    added = 0
    odd_letter = ''
    for k, v in letters.items():
        if v & 1 == 1:
            odd_letter = k
            continue
        added += v
        half = v // 2
        # 0 - 1
        ans[start: start+half] = [k] * half
        # -2 - -1
        ans[end - half: end] = [k] * half
        start += half
        end -= half

    if odd:
        to_add = len(ans) - added
        added //= 2
        if len(ans) == 0:
            ans = [odd_letter] * to_add
        else:
            ans[added:added+to_add] = [odd_letter] * to_add

    print(''.join(ans))



