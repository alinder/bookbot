def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)
    word_count = count(text)
    print(f"{word_count} words found in the document")
    per_letter = count_per_letter(text)
    print(per_letter)
    count_report = report(per_letter)
    for each in count_report:
        print(f"The '{each["name"]}' character was found {each["num"]} times")



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


def report(per_letter):
    letter_list = []
    for letter in per_letter:
        if letter[0].isalpha():
            added_letter = {}
            added_letter["name"] = letter
            added_letter["num"] = per_letter[letter]
            letter_list.append(added_letter)
    
    def sort_on(dict):
        return dict["num"]
    letter_list.sort(reverse=True, key=sort_on)
    return letter_list
    
    print(letter_list)


main()