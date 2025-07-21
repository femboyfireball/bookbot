def get_word_count(string):
    string_list = string.split()
    return len(string_list)

def get_characters_count(string):
    characters = dict()
    for character in string:
        if not character in characters:
            characters[character] = 1
        else:
            characters[character] += 1
    return characters
