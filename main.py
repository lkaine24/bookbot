def read_book(path):
    # Open file and assign contents to file_contents
    with open(path) as f:
        file_contents = f.read()
        
        return file_contents

def get_word_count(words):
    # Split words into list, and obtain the number of indicies in that list to get the word count
    wc = len(words.split())
    return wc

def get_char_count(words):
    # Alter all characters to lowercase and assign to lower_chars
    lower_chars = words.lower()

    char_count = {}

    # For each character
    for char in lower_chars:
        # If the character is alphanumeric, but isn't a number, add it as a key to char_count and set its value to 1
        if char not in char_count and char.isalnum() == True and char.isdigit() == False:
            char_count[char] = 1
        # If the character is already a key in char_count, add one to its value
        elif char in char_count:
            char_count[char] += 1

    return char_count

def print_report(book_name, word_count, char_count):
    print(f'--- Begin report of {book_name} ---')
    print(f'There are a total of {word_count} words found in the document.')

    # Sort all keys in char_count
    sorted_chars = sorted(char_count.keys())

    # For each character in sorted_chars, print the character and its value to the terminal
    for char in sorted_chars:
        print(f'The {char} character was found {char_count[char]} times')


def main():
    path = "books/frankenstein.txt"
    words = read_book(path)
    word_count = get_word_count(words)
    char_count = get_char_count(words)
    print_report(path, word_count, char_count)

if __name__ == '__main__':
    main()