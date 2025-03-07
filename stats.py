def get_num_words(content):
    words = content.split()
    return len(words)


def char_count_map(content):
    chars = {}
    for char in content:
        lowered = char.lower()
        if lowered not in chars:
            chars[lowered] = 1
        else:
            chars[lowered] += 1

    return chars


def sort_characters(char_dict):
    char_list = []

    for char, count in char_dict.items():
        char_list.append({"char": char, "count": count})

    def sort_on(dict):
        return dict["count"]

    char_list.sort(reverse=True, key=sort_on)

    return char_list
