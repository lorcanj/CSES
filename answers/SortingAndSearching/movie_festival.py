n = int(input())
films = []
for _ in range(n):
    pair = tuple(map(int, input().split()))
    films.append(pair)

films = sorted(films, key= lambda x: x[1])

film_index = 0
curr_end = -1
ans = 0

# focus on the film endings and take a greedy approach
# always choose the next film with the earliest end that starts after the current end
while film_index < len(films):
    if films[film_index][0] >= curr_end:
        ans += 1
        curr_end = films[film_index][1]
    film_index += 1
print(ans)