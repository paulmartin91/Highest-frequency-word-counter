user_input = input("Please enter file name or directory: ")
text_file_to_check = open(user_input)

word_histogram = dict()

for line in text_file_to_check:
    line_splitted_into_words = line.split()
    for word in line_splitted_into_words:
        word_histogram[word] = word_histogram.get(word, 0) +1

largest_current_word = dict()
largest_current_word_count = 0

for word,count in word_histogram.items():
    if count > largest_current_word_count:
        largest_current_word = {word: count}
        largest_current_word_count = count

print(largest_current_word)