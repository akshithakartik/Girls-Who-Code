sentence = input("Enter the sentence: ")  # the sentence entered by the user
sentence = sentence.casefold()  # converting the sentence to lowercase for comparison
count = {i: 0 for i in
         'aeiou'}  # creates a dictionary with the keys as vowels(a,e,i,o,u) and values as 0(to begin with)
for char in sentence:  # iterate over the sentence using a for loop
    if char in count:  # checks if the character in the sentence matches a vowel
        count[char] += 1  # increases the count/value of the corresponding vowel in the dictionary by 1
print(count)  # displays the final dictionary with count of each vowel
