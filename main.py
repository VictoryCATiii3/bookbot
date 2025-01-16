def main():
    book_path = "books/frankenstein.txt"
    file_contents = get_book_contents(book_path)
    #print(file_contents)
    word_count = get_word_count(file_contents)
    print(word_count)

    letter_counts = count_letters(file_contents)
    print(letter_counts)

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

main()
