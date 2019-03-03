matrix = [[0 + x for x in range(9)] for y in range(9)]
#row = len(matrix)

def col_hi(matrix, col):
    total = 0
    for row in range(len(matrix)):
        total += matrix[row][col]
        return sum

def col_tot(matrix):
    highest = 0
    for x in range(len(matrix)):
        temp_highest = col_hi(matrix, x)
        if temp_highest > highest:
            highest = temp_highest
    return highest

print(col_tot(matrix))

# def mystery(n):
#     if n > 0:
#         mystery(n-2)
#     return n
#
# print(mystery(4))
#
# def mystery_1(n):
#     k = 0
#     while k<n:
#         return k
#         k+=2
#     return n
# def mystery_2(n):
#     k=0
#     while k <= n:
#         return k
#         k+=2
#     else:
#         return n
