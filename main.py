import sys

def read_file_to_string(filepath) -> str:
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def word_count(words) -> int:
    word_split = words.split()
    return len(word_split)

def char_count(words) -> dict:
    words = words.lower()
    hashmap = {}
    for letter in words:
        if letter in hashmap:
            hashmap[letter] += 1
        else:
            hashmap[letter] = 1
    return hashmap


def main() -> int:
    path_to_file = "books/frankenstein.txt"

    file_contents = read_file_to_string(path_to_file)
    char_dict = char_count(file_contents)

    # print(file_contents)
    # print(word_count(file_contents))
    # char_count(file_contents)
    header = (f"--- Begin report of {path_to_file} ---")
    words_found = (f"{word_count(file_contents)} words found in the document")
    

    print(header)
    print(words_found)
    print()
    for key in char_dict:
        if key.isalpha():
            print(f"The '{key}' character was found {char_dict[key]} times")
    print(f"--- End report ---")


    return 0

if __name__ == '__main__':
    sys.exit(main())