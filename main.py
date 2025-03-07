from stats import get_num_words, char_count_map


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def main():
    book_path = "./books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    print(char_count_map(text))


main()
