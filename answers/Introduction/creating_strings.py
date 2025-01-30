import math

s = input()
l = list(s)
input_length = len(s)
unique_values = set(letter for letter in s)
unique_values_length = len(unique_values)
output = []

letter_counts = {}
for char in s:
    if char not in letter_counts:
        letter_counts[char] = 0
    letter_counts[char] += 1

denominator = 1

for v in letter_counts.values():
    denominator *= math.factorial(v)

def create_strings(input_string: list, curr: list):
    if len(input_string) == 0:
        output.append(curr.copy())
        return

    for i in range(len(input_string)):
        temp = input_string.copy()
        letter = temp.pop(i)
        curr.append(letter)
        create_strings(temp, curr)
        curr.pop()


create_strings(l, [])
print(math.factorial(input_length) // denominator)

unique_output = set()
actual_output = []

for o in output:
    word = ''.join(o)
    if word not in unique_output:
        actual_output.append(word)
        unique_output.add(word)
actual_output.sort()

for w in actual_output:
    print(w)
