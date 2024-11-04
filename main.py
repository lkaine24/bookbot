def read_book(path):
    # Open file and assign contents to file_contents
    with open(path) as f:
        file_contents = f.read()
        
        return file_contents

def get_word_count(words):
    # Split words into list, and obtain the number of indicies in that list to get the word count
    wc = len(words.split())
    return wc

def main():
    words = read_book("books/frankenstein.txt")
    print(get_word_count(words))

if __name__ == '__main__':
    main()