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
