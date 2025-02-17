def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)
    word_count = count(text)
    print(f"{word_count} words found in the document")
    print(count_per_letter(text))



def get_book_text(path):
    with open(path) as f:
        return f.read()

def count(text):
    return len(text.split())

def count_per_letter(text):
    text_lower = text.lower()
    total = {}
    for letter in text_lower:
        if letter in total:
            total[letter] += 1
        else:
            total[letter] = 1
    return total

main()