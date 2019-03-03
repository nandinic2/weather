# make random array
import random
arr = [random.randint(0,1000) for x in range(100)]
# sort array
def sorting(arr):
    n = len(arr)
    for i in range(n):
        # traverse the array from 0 to n-i-1
        swap = False
        for j in range(0, n-i-1) :
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap = True
                #swap if next element is greater
        if swap == False:
            break
            # stops if no swap is needed.
    return arr
print(sorting(arr))
