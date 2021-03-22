def vowelCount(string:str):

    vowels = 'aeiou' # Vowel string for English
    string = string.casefold() # not .lower() because we can enter an ß - symbol or similar.
    count = {}.fromkeys(vowels, 0) # Define a dict with vowels string and initial values 0
    print (count)
    print (type(count))
    for character in string:
        if character in count:
            count[character] += 1

    return count

usr_str = input("Enter a string!\n")
print(vowelCount(usr_str))