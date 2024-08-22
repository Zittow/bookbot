def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    report = get_report(num_words, chars_dict, book_path)
    print(report)
 
def get_report(num_words, chars_dict, book_path): 
    nl = '\n'
    header = f"--- Begin report of {book_path} ---{nl}"
    word_count = f"{num_words} words found in the document{nl}{nl}"
    
    sorted_items = sorted(chars_dict.items(), key=lambda item: item[1], reverse=True)
    
    char_counts = [
        f"The '{char}' character was found {count} times"
        for char, count in sorted_items if char.isalpha()
    ]
    
    clean_text = header + word_count + nl.join(char_counts) + nl
    return clean_text


def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()