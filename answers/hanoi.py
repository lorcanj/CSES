size = int(input())
minimum = 2 ** size - 1

# i.e. want n-1 on the middle, which means n-2 on the other free, which means n-3 on the middle... which
# means move the smallest over to what we've determined

def tower_of_hanoi(n, source, destination, auxiliary):
    if n == 1:
        print(f"{source} {destination}")
        return
    tower_of_hanoi(n - 1, source, auxiliary, destination)
    # this means to move the largest disk to the destination as we have moved n-1 disks to the
    # auxiliary free space
    print(f"{source} {destination}")
    tower_of_hanoi(n - 1, auxiliary, destination, source)
print(minimum)
tower_of_hanoi(size, 1, 3, 2)