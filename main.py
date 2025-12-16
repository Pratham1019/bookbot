from stats import get_num_words, get_character_count_dict, sort_dict
import sys

def get_book_text(filepath: str) -> str:
    with open(filepath) as file:
        file_contents = file.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1) 
    
    
    filepath = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    
    file_content = get_book_text(filepath)
        
    print("----------- Word Count ----------")
    word_count = get_num_words(file_content)
    print(f"Found {word_count} total words")
    
    print("--------- Character Count -------")
    char_dict = get_character_count_dict(file_content)
    
    sorted_char_list = sort_dict(char_dict)
    
    for item in sorted_char_list:
        print(f"{item["char"]}: {item["count"]}")
        
    print("============= END ===============")

if __name__ == "__main__":
    main()
    
