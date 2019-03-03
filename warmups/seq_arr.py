#array = [1,2,3,4,5,6,7,8,9,10]
#value = 6
# RETURNING INDEX VALUE
#def search(arr, val):
#    count = -1
#    for n in arr:
#    increments per value
#        count += 1
#        if n == val:
#            return count
#            returns index value


#print(search(array, value))

#RECURSION, RETURNING TRUE OR FALSE
#arr = [1,2,3,4,5,6,7,8,9,10]
#val = 10

#def search(arr, val):
#    ans = False
#    mid = arr[len(arr)//2]
#    if val == mid:
#        ans = True
#        return ans
#    if val < mid:
#        return search(arr[:len(arr)//2], val)
#    elif val > mid:
#        return search(arr[len(arr)//2+1:], val)

#print(search(arr, val))

#ITERATIVE, RETURN TRUE OR False
array = [1,2,3,4,5,6,7,8,9,10]
value = 10
def search(arr, val):
    mid = len(arr)//2
    high = len(arr)-1
    while mid != val:
        # condition for if val is not in the list
        # condition for if val is greater than mid
        # change value of mid, high or both
        if high == mid:
            return "not there"
        if val > arr[mid]:
            new_mid = (high+mid+1)/2
            return mid
        if val < arr[mid]:
            mid =


        # condition for is val is less than mid

print(search(array, value))
