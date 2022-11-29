sentence = input("Enter the sentence: ")    # the sentence entered by the user
sentence = sentence.casefold()  # converts the sentence to lowercase for comparison
count = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}    # create a dictionary with the vowels as keys and initial values as 0
for char in sentence:   # iterates through the sentence using for loop
    if char in count:   # checks if the character in the sentence matches any vowel in count
            count[char] += 1   # if so, increases the value of the corresponding vowel in the dictionary by 1
print(count) # displays the final dictionary
