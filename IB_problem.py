a = [[7,0,0,0,0,0], [0,0,0,0,0,0], [0,0,-3,0,9,0], [0,0,0,0,0,0], [0,0,-1,0,0,0], [0,-6,0,0,-5,1]]

def first_arr(arr):
    new_arr = []
    for row in range(len(arr)):
        for col in range(len(arr)):
            if arr[row][col] != 0:
                new_arr.append(arr[row][col])
    return new_arr

print(first_arr(a))

def second_arr(arr):
    new_arr = []
    row_count = []
    count = 0
    for row in range(len(arr)):
        for col in range(len(arr)):
            if arr[row][col] != 0:
                count += 1
                new_arr.append(count)

    return new_arr

print(second_arr(a))
