import binary_hash

b_hash = binary_hash.binary_hash

for key, value in b_hash.items():
    print(key,value)

for key, value in b_hash.items():
    if key == "x":
        print(value)
