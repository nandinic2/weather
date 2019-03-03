import random

#passengers = [[random.randint(0,100) for x in range(6)] for y in range(29)]
#print(passengers)
#monday = [random.randint(200,201) for x in range(29)]
#print(monday)

# updating all mondays in passengers

#for day in range(len(monday)):
#    passengers[day][0] = monday[day]

#print(passengers)

passengers = [[0 + x for x in range(8)] for y in range(8)]

print(passengers)

#def d_total(col_num, matrix):
#    total = 0
#    for day in range(len(matrix)):
#        total += passengers[day][col_num]
#    return total
#print(d_total(1, passengers))

def diagonal(matrix):
    total = 0
    for row in range(len(matrix)):
        total += matrix[row][row]
    return total

print(diagonal(passengers))

def inv_diagonal(matrix):
    total = 0
    count = len(matrix)
    for row in range(len(matrix)):
        count -= 1
        total += matrix[count][count]
    return total

print(inv_diagonal(passengers))
