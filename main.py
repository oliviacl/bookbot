import sys
from stats import get_num_words, char_count_map, sort_characters


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_counts = char_count_map(text)
    sorted_char_counts = sort_characters(char_counts)

    print_report(book_path, num_words, sorted_char_counts)


def print_report(book_path, num_words, char_counts):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at  {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in char_counts:
        char, count = item["char"], item["count"]
        if not char.isalpha():
            continue
        print(f"{char}: {count}")
    print("============= END ===============")


main()
