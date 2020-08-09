user_input_filename = input("Enter file name or directory: ")
file_to_work_with = open(user_input_filename)

word_histogram = dict()

for line in file_to_work_with:
    line_splitted_to_words = line.split()
    for word in line_splitted_to_words:
        word_histogram[word] = word_histogram.get(word, 0) +1

word_histogram_reverse_values = list()

for key, value in word_histogram.items():
    word_histogram_reverse_values.append((value, key))

word_histogram_reverse_values_sorted = sorted(word_histogram_reverse_values, reverse=True)

while True:
    user_input_place_ammount = input("Number of places: ")
    try:
        int(user_input_place_ammount)
        break
    except:
        print("Whole integers only please!")
        continue

for key, value in word_histogram_reverse_values_sorted[:int(user_input_place_ammount)]:
    print(key, value)