a = input("Insert a word to convert to pig latin: ")

def piglatin(word):
    for char in range(0, len(word)):
        b = word[char]
        if char == 0 and (b == "a" or b == "e" or b == "i" or b == "o" or b == "u"):
            word = word + "way"
            break
        elif b == "a" or (b == "e" or b == "i" or b == "o" or b == "u"):
            save = word[:char]
            word = word[char:] + save + "ay"
            break
    return word

print(piglatin(a))