array = input()
if len(array) == 0:
    print(0)

max_found = 0
index = 0
current_char = array[0]
temp_count = 0
while index < len(array):
    this_char = array[index]
    if this_char == current_char:
        temp_count += 1
        index += 1
        continue
    
    current_char = this_char
    max_found = max(max_found, temp_count)
    temp_count = 1
    index += 1

print(max(max_found, temp_count))

