from stats import get_word_count, get_characters_count


def sort_on(dictionary):
    return dictionary["Count"]

def get_book_contents(book_path):
    with open(book_path) as f:
        book_contents = f.read()
        return str(book_contents)

def main():

    book = "books/frankenstein.txt"
    book_contents = get_book_contents(book)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}")

    word_count = get_word_count(book_contents)
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")

    character_counts = get_characters_count(book_contents.lower())
    character_counts_list = []
    for character in character_counts:
        character_dict_form = {
            "Character" : character,
            "Count" : character_counts[character]
        }
        character_counts_list.append(character_dict_form)

    character_counts_list.sort(reverse=True, key=sort_on)
    print("--------- Character Count -------")
    for character in character_counts_list:
        if character["Character"] == "\n":
            print(f"\\n: {character["Count"]}")
        else:
            print(f"{character["Character"]}: {character["Count"]}")
main()
