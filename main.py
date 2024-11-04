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
    lower_chars = words.lower()

    char_count = {}

    for char in lower_chars:
        if char not in char_count and char.isalnum() == True and char.isdigit() == False:
            char_count[char] = 1
        elif char in char_count and char.isalnum() == True and char.isdigit() == False:
            char_count[char] += 1

    return char_count


def main():
    words = read_book("books/frankenstein.txt")
    word_count = get_word_count(words)
    char_count = get_char_count(words)
    print(char_count)

if __name__ == '__main__':
    main()