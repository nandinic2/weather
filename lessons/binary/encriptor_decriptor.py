import binary_hash

b_hash = binary_hash.binary_hash
#name of file and data structure
#print(b_hash)

def encript(message):
    ans =[]
    message = list(message)
    for letter in message:
        letter = b_hash[letter]
        ans.append(letter)
    ans = "-".join(ans)
    return ans

words = encript("hello")

def decript(b_num):
    ans = []
    # chunk out binary
    b_num = b_num.split("-")
    for num in b_num:
        for key, value in b_hash.items():
            if value == num:
                num = key
            print(ans)

decript(words)
