def main():
    book_path = "books/frankenstein.txt"
    file_contents = get_book_contents(book_path)
    #print(file_contents)
    words = file_contents.split()
    print(len(words))


def get_book_contents(book_path):
    with open(book_path) as f:
        file_contents = f.read()
    return file_contents

main()
