# Open and read files
file = open("josefile.txt", "r")
text = file.read()

# Count number of lines in file
numOfLines = text.count("\n") + 1
print("Number of lines:", numOfLines)

# Count number of words in lines
words = text.split(' ')
numOfWords = len(words)
print("Number of words:", numOfWords)

# Count the number of characters (including whitespace) in the file and print it
numOfCharacters = len(text)
print("Number of characters:", numOfCharacters)

# Determine the average word length in the file and print it
total_word_length = sum(len(word) for word in words)
average_word_length = total_word_length / numOfWords if numOfWords > 0 else 0
print("Average word length:", average_word_length)

# Determine the most common word in the file and print it
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

most_common_word = max(word_count, key=word_count.get)
print("Most common word:", most_common_word)

# Create a new file called "analysis.txt" and write the analysis results to it
with open("analysis.txt", "w") as analysis_file:
    analysis_file.write(f"Number of lines: {numOfLines}\n")
    analysis_file.write(f"Number of words: {numOfWords}\n")
    analysis_file.write(f"Number of characters: {numOfCharacters}\n")
    analysis_file.write(f"Average word length: {average_word_length}\n")
    analysis_file.write(f"Most common word: {most_common_word}\n")

print("Analysis results have been written to analysis.txt.")
