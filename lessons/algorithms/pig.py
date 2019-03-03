def pig_latin(str):
    new = str.lower()
    letters = list(new)
    count = -1
    for n in letters:
        count += 1
        # if letters[count] != 'a' or 'e' or 'i' or 'o' or 'u':
        #     letters.append(letters[count])
        #     print(letters)
        #     del letters[count]
        if count[0] == 'a' or 'e' or 'i' or 'o' or 'u':
            letters.append(letters[count])
            print(letters)
            del letters[count]

        print(letters)
        letters.append("ay")
        print(letters)
        combined = ''.join(letters)
        return combined
    else:
        letters.append('ay')
        print(letters)



# pig_latin('Map') #apmay
pig_latin('Egg') #eggay
