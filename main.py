from stats import get_word_count, get_characters_count

def get_book_contents(book_path):
    with open(book_path) as f:
        book_contents = f.read()
        return str(book_contents)

def main():
    book_contents = get_book_contents("books/frankenstein.txt")
    word_count = get_word_count(book_contents)
    print(f"{word_count} words found in the document")
    print(get_characters_count(book_contents.lower()))

main()
