# Your project code here

import random
items_1 = [["Samosa","Beetroot Kebab","Sabudana Vada","Mini Idli"],["Begun Bhaja","Daal Makhani","Chana","Bhindi"],["Butter Chicken","Shosher machh","Butter Chicken","Steamed illish"],["Gajar Roti","Paratha","Roti","Naan"]]
# Sets the values in  items_1
items_2 = [["Aloo Gobhi", "Malai Kofta", "Fried Bhindi", "Karela"],[ "Prawn Malai Curry","Mutton Curry","Chicken Curry","Kebab"],["Pulao","Jeera Rice", "Pulao", "Jeera Rice"],["Gulab Jamun","Halwa", "Mishti Doi","Kheer"]]
# Sets the values in  items_2

def menu_1(arr):
    app = random.choice(arr[0])
    veg = random.choice(arr[1])
    non_veg = random.choice(arr[2])
    side = random.choice(arr[3])
    # Chooses one value from each row in matrix
    menu_1 = app+", "+ side+", "+veg+", "+non_veg+", "
    # Puts the chosen variables in order
    return menu_1
    # outputs order

def menu_2(arr):
    veg_2 = random.choice(arr[0])
    non_veg_2 = random.choice(arr[1])
    side_2 = random.choice(arr[2])
    des = random.choice(arr[3])
    # Chooses one value from each row in matrix
    menu_2 =  veg_2+", "+non_veg_2+", "+side_2+", "+des
    # Puts the chosen variables in order
    return menu_2
    # outputs order

x = menu_1(items_1)
# calls the function using items_1 and sets it to the variable x
y = menu_2(items_2)
# calls the function using items_2 and sets it to the variable y

def final(x,y):
    return x + y
    # Adds both menus and outputs the final menu

print(final(x,y))
# calls the final function
