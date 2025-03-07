from stats import get_num_words


def get_book_text(filepath):
    with open(filepath) as f:
        file_content = f.read()
        return file_content


def main():
    book_content = get_book_text("./books/frankenstein.txt")
    num_words = get_num_words(book_content)
    print(f"{num_words} words found in the document")


main()
