def num(n):
    count = 0
    count = int(n/10)
    # stores how many times 10 goes into the number in integer form.
    r = n % 10
    count += int(r/5)
    # stores how many times 5 goes into remainder in integer form.
    r = r % 5
    count += r
    # adds all the counts and the remainder
    return count

print(num(13))
