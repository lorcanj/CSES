number = int(input())

output = ['0', '1']
for i in range(2, number+1):
    output = [e + '0' for e in output] + [e + '1' for e in reversed(output)]

for code in output:
    print(code)




