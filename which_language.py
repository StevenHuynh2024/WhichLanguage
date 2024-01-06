import math
input = input("Text: ").lower().strip(" ")
file = open("input2.txt")
dict = {}
letter_dict = {}
frequency_dict = {}
languages = ["English", "French", "German", "Spanish", "Portuguese", "Esperanto", "Italian", "Turkish",
             "Swedish", "Polish", "Dutch", "Danish", "Icelandic", "Finnish", "Czech", "Hungarian"]
greatest = 0
greatest_letter = ""
# Sets an initial dict for every unique letter in the input
for words in input:
    for letters in words:
        letter_dict[letters] = 0
# Counts the amount of time each letter occurs
for words in input:
    for letters in words:
        letter_dict[letters] = letter_dict[letters]+1
# Finds the frequency of each letter in regards to the input
for stuff in letter_dict:
    frequency_dict[stuff] = float(letter_dict[stuff]/len(input.strip(" ")))
# Finds the letter that occurs the most excluding spaces
for items in frequency_dict:
    if items != " ":
        if frequency_dict[items] > greatest:
            greatest = frequency_dict[items]
            greatest_letter = items


lowest_score = 10000
chi_score = 0
output = 0
expected = 0
language_index = 0
# the actual code
for language in range(len(languages)):
    chi_score = 0
    for letter in letter_dict:
        output = frequency_dict[letter]
        file.seek(0)
        for lines in file:
            lines = lines.split(",")
            if letter == lines[0]:
                expected = float(lines[1+language].strip("~\n*%"))/float(100)
                if expected != 0:
                    chi_score += float(math.sqrt(((expected - output) ** 2)/expected))
    if chi_score < lowest_score:
        lowest_score = chi_score
        language_index = language


print(languages[language_index])
print(lowest_score)


