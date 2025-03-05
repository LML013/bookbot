import sys
from stats import word_count

def read_file_to_string(filepath) -> str:
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def char_count(words) -> dict:
    words = words.lower()
    hashmap = {}
    for letter in words:
        if letter in hashmap:
            hashmap[letter] += 1
        else:
            hashmap[letter] = 1
    return hashmap


def main(filepath) -> int:
    # path_to_file = "books/frankenstein.txt"


    file_contents = read_file_to_string(filepath)
    char_dict = char_count(file_contents)

    # print(file_contents)
    # print(word_count(file_contents))
    # char_count(file_contents)
    header = (f"--- Begin report of {filepath} ---")
    words_found = (f"{word_count(file_contents)} words found in the document")
    

    print(header)
    print(words_found)
    print()
    for key in char_dict:
        if key.isalpha():
            print(f"{key}: {char_dict[key]}")
    print(f"--- End report ---")


    return 0

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    sys.exit(main(sys.argv[1]))