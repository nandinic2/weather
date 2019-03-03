import random
arr = [random.randint(0,1000) for x in range(100)]
print(arr)
def reverse(arr):
    new_arr = []
    count = len(arr)-1
    for j in arr:
        count -= 1
        new_arr.append(arr[count+1])

    return new_arr

print(reverse(arr))
