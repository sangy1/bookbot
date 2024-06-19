path_to_file = "books/frankenstein.txt"
file_contents = ""

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_word_count(text):
    words = text.split()
    return len(words)
    
def word_dict_count_in_text(text):
    word_dict = {}
    words = text.lower()
    for word in words:
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1
    return word_dict

def sort_dictionary_alpha(word_dict):
    alpha_dict = {}
    # Gets new dictionary with only letters
    for char in word_dict:
        if char.isalpha():
            alpha_dict[char] = word_dict[char]
    
    sorted_list = sorted(alpha_dict.items(), reverse=True, key = lambda x:x[1])
    return sorted_list
    

def main():
    text = get_book_text(path_to_file)
    count = get_word_count(text)
    word_dict = word_dict_count_in_text(text)
    sorted_list = sort_dictionary_alpha(word_dict)
        
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count} words found in the document")
    for list_dict in sorted_list:
        print(f"The '{list_dict[0]}' character was found {list_dict[1]} times")
    print(f"--- End report ---")

    
    
    
main()