def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = get_book_words(text)
    print(words)
    character_count = get_book_character_count(text)
    print(character_count)

def get_book_words(text):
    count = len(text.split())
    return count

def get_book_character_count(text):
    alphabet_dict={}
    for character in text:
        character = character.lower()
        if character.isalpha():
            if character in alphabet_dict:
                alphabet_dict[character] += 1
            else:
                alphabet_dict[character] = 1
    return(alphabet_dict)

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
