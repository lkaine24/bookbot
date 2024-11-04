def read_book(path):
    with open(path) as f:
        file_contents = f.read()
        
        print(file_contents)

def main():
    read_book("books/frankenstein.txt")

if __name__ == '__main__':
    main()