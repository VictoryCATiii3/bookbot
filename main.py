def main():
    book_path = "books/frankenstein.txt"
    file_contents = get_book_contents(book_path)
    #print(file_contents)
    word_count = get_word_count(file_contents)
    print(f"{word_count} words were found in the document")
    letter_counts = count_letters(file_contents)

    print_count(letter_counts)

def get_book_contents(book_path):
    with open(book_path) as f:
        file_contents = f.read()
    return file_contents

def get_word_count(str_in):
    words = str_in
    return len(words)

def count_letters(str_in):
    letter_counts = {}
    tmp_str = str_in.lower()
    for letter in tmp_str:
        if letter in letter_counts:
            letter_counts[letter] = letter_counts[letter] + 1
        else:
            letter_counts[letter] = 1
    return letter_counts

def print_count(letter_counts):
    sorted_count = sorted(letter_counts.items(), key=lambda item:item[1], reverse=True)
    for item in sorted_count:
        if item[0].isalpha():
            print(f"The '{item[0]}' character was found {item[1]} times")

main()
