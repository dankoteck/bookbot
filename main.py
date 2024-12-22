def main():
    contents = get_file_contents()
    total_words = get_total_words(contents)
    char_dict = get_characters_dictionary(contents)
    sorted_char_dict = sort_characters_dictionary(char_dict)
    print_report(total_words, sorted_char_dict)


def get_total_words(contents):
    return len(contents.split())


def get_file_contents():
    with open('./books/frankenstein.txt') as f:
        return f.read()


def get_characters_dictionary(contents):
    char_list = list(contents)
    char_dict = {}
    for char in char_list:
        current_char = char.lower()
        if current_char.isalpha():
            if current_char in char_dict:
                char_dict[current_char] += 1
            else:
                char_dict[current_char] = 1
    return char_dict


def sort_characters_dictionary(char_dict):
    sorted_dict = {}
    for key in sorted(char_dict, key=char_dict.get, reverse=True):
        sorted_dict[key] = char_dict[key]
    return sorted_dict


def print_report(words, char_dict):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words} words found in the document\n")

    for char in char_dict:
        print(f"The '{char}' character was found {char_dict[char]} times")
    print("--- End report ---")

main()
