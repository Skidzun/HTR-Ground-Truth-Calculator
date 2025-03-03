with open('../data/GT.txt', 'r', encoding='utf8') as f:
    text = f.read() # saves GT into a variable to calculate numbers of characters and words

# Caculate the number of characters
number_char = len(text)

# Calculate the number of words
text_tokenised = text.split() # splits the text into single tokens
number_words = len(text_tokenised) # counts the tokens

# Calculate the number of lines
with open('../data/GT.txt', 'r', encoding='utf8') as f:
    text_lines = f.readlines() # saves lines into variable
number_lines = len(text_lines) # counts lines

# Print results
print(f'number of characters: {number_char}')
print(f'number of words: {number_words}')
print(f'number of lines: {number_lines}')

# Create a csv file with results
import csv
import os

with open('../data/GT-total.csv', 'w', encoding='utf-8', newline='') as f: # Beware: this will create a new file and overwrite any existing file with the same name
    writer = csv.writer(f, delimiter=',') #if you wish to append an existing file, change 'w' to 'a'

    # Write header
    header = ['ID', 'Corpus', 'Zeichen', 'Wörter', 'Zeilen'] # delete this section if you append an existing file
    writer.writerow(header) # if appending, delete this as well

    # Write line
    ID =+ 1
    row = [ID, 'Urkunden Reg.F.III', number_char, number_words, number_lines] # change corpus name if appending
    writer.writerow(row)
