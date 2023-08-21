def consonant_value_checker(word):
    consonants = "bcdfghjklmnpqrstvwxyz" 
    current_value = 0
    max_value = 0
   
    for letter in word:
        if letter in consonants:
            current_value += ((ord(letter) - ord("a")) + 1)
            max_value = max(max_value, current_value)
         
        else: 
            current_value = 0

    return max_value


input_word = input("Enter a String: ")

result = consonant_value_checker(input_word)

print(result)

 