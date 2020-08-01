from cs50 import get_string


sentences = get_string("Text: ")
num_letters = 0
for letter in sentences:  # count the number of letters
    if letter.isalpha():
        num_letters += 1

num_words = sentences.count(" ") + 1  # calculate the number of words
num_sentences = sentences.count(".") + sentences.count("!") + sentences.count("?")  # calculate the number of sentences

L = (num_letters/num_words)*100
S = (num_sentences/num_words)*100
grade_level = 0.0588 * L - 0.296 * S - 15.8  # compute the Coleman-Liau index

if (grade_level >= 16):
    print("Grade 16+")
elif (grade_level < 1):
    print("Before Grade 1")
else:
    print("Grade", round(grade_level))
