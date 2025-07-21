def get_book_contents(book_path):
    with open(book_path) as f:
        book_contents = f.read()
        return str(book_contents)

def main():
    book_contents = get_book_contents("books/frankenstein.txt")
    print(book_contents)

main()
