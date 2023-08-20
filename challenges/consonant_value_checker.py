def consonant_value_checker(word):
    vowels = "AaEeiIOoUu"
    str2 = ""

    for letter in word:
        if letter not in vowels:
            str2 = str2+letter
            return(str2)

print(consonant_value_checker("hello"))


    
    # if word != vowels:
    #     r
    
    # for i in word:
    #     if i == vowels:
    # print (int(word - vowels))
            
# print(consonant_value_checker("hello"))
# def albabet_counter(letter):
#     if letter != "a" and letter != "b":
#         return(letter)
#     else:
#         return(letter - "a" - "b")


# alphabet = ["a", "b", "c", "d"]
# alphabet_numbers = [letter for letter in alphabet if letter != "a" and letter != "b"]
# print(alphabet_numbers)
    
# print(albabet_counter("adele"))
# # print(consonant_value_checker())
 