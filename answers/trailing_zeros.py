number = int(input())
actual_number = number

ans = 0
power = 1
calculate = power
while (calculate := 5 ** power) <= number:
    ans += number // calculate
    power += 1
    
print(ans)


# 2 shows up more than 5 in the prime factorisation of the numbers
# so the answer should be the number of times that 5 shows up in the interval of 1..N
# 1 , 2, 3 , 4, 5, 6, 7, 8 , 9, 10
# 5   10  15 20 25 30 35 40  45 50

# 50 = 5 * 10 = 5 * 5 * 2
# under counting 5 * 5 * (2,3,4)

# do we keep dividing by powers of 5? that should give the right answer
# missing the numbers in between
# 5 * 5 = 25 = 2
# 5 * 6 = 30 = 1

# divide by 5 removes 1 layer of 5s from the factorisation
# need to check for further powers of 5, e.g. 5^2 to count extra 5s in 25, 50, 75...