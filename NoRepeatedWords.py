def filter_words(s):
    lower_s = s.lower()
    filtered_letters = [char for char in lower_s if char.isalpha()]
    return len(filtered_letters) == len(set(filtered_letters))

input_string = input()
if filter_words(input_string):
    print("true")
else:
    print("false")