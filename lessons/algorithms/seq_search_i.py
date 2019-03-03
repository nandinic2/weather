arr = [1,2,3,4,5,6,7,8,9,10]
val = 9

def search(arr, val):
    mid = arr[len(arr)/2]
    hi = arr[-1]
    while mid != hi:
        if mid == hi:
            return -1
        elif arr[mid] > val:
            hi = mid
            mid = mid//2
        elif arr[mid] < val:
            mid = (mid+1+hi)//2
    return mid
