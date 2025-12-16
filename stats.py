def get_num_words(text: str) -> int:
    words = text.split()
    return len(words)

def get_character_count_dict(text: str) -> dict:
    dictionary = {}
    
    for i in range(0, len(text)):
        current_char = text[i].lower()
        if current_char in dictionary:
            dictionary[current_char] += 1
        else:
            dictionary[current_char] = 1
    
    return dictionary

def get_count(dict: dict) -> int:
    return dict["count"]

def sort_dict(char_dict: dict) -> list:
    '''
        1. convert each entry of the dict into a dict of itself and send to a list
        2. sort the list
        3. return the list
    '''
    
    list = []
    
    for key, value in char_dict.items():
        if key.isalpha():
            new_dict = {
                "char": key,
                "count": value
            }
            
            list.append(new_dict)
    
    
    list.sort(reverse=True, key=get_count)
    return list



