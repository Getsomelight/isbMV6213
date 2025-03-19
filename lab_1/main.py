import json
import argparse

def parse()->argparse.Namespace:
    """
    Handle argument parsing and return them
    Raises SyntaxError if no filenames is provided
    """
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument('config_1', type=str)
        parser.add_argument('key_1_name', type=str)
        parser.add_argument('config_2', type=str)
        parser.add_argument('frequency_ru', type=str)
        return parser.parse_args()
    except:
        raise SyntaxError("Path is empty")


def open_file(name)->str:
    """
    Open and read the input file
    Raises FileNotFoundError if the file cannot be found
    """
    try:
        with open(name, "r", encoding="UTF-8") as file:
            return file.read()
    except:
        raise FileNotFoundError("File doesnt found or doesnt exist")

def save_file(path: str, output: str)->None:
    """
    Open and write the output file
    Raises Exception if the file cannot be found
    """
    try:
        with open(path, 'w', encoding='UTF-8') as file:
            file.write(output)
    except:
        raise Exception("Cannot create output file")

def open_json_file(name: str)->dict:
    """
    Open and read the content of the JSON file
    Raises FileNotFoundError if the JSON file cannot be found
    """
    try:
        with open(name, "r", encoding="UTF-8") as file:
            return json.load(file)
    except:
        raise FileNotFoundError("File doesnt found or doesnt exist")

def save_json_file(path: str, info)->None:
    """
    Open and write the content of the JSON file
    Raises Exception if the JSON file cannot be found
    """
    try:
        with open(path, 'w', encoding='UTF-8') as file:
            json.dump(info, file, ensure_ascii=False, indent=4)
    except:
        raise Exception("Cannot create output JSON file")

def encrypt(text: str, alphabet: str, offset: int)->str:
    """
    Encrypting input text
    """
    encrypted_text = ""
    for i in text:
        if i in alphabet:
            encrypted_text += alphabet[(alphabet.index(i) + offset) % len(alphabet)]
        else:
            encrypted_text += i
    return encrypted_text

def frequency_analysis(text: str, frequency_ru: dict)->tuple:
    """

    """
    text = text.upper()
    char_text = {}
    for char in text:
        if char not in char_text:
            char_text[char] = 0
        char_text[char] += 1
    total_chars = len(text)
    frequency_text = {char: count / total_chars for char, count in char_text.items()}
    sorted_frequency_text = sorted(frequency_text.items(), key=lambda x: x[1], reverse=True)
    sorted_frequency_ru = sorted(frequency_ru.items(), key=lambda x: x[1], reverse=True)
    key = {}
    for i, (my_char, _) in enumerate(sorted_frequency_text):
        if i < len(sorted_frequency_ru):
            ru_char, _ = sorted_frequency_ru[i]
            key[my_char] = ru_char
        else:
            key[my_char] = ""
    return frequency_text, key

def decrypt(text: str, key: dict)->str:
    """
    Decrypting
    """
    text = text.upper()
    decrypted_text = ""
    for i in text:
        if i in key:
            decrypted_text += key[i]
        else:
            decrypted_text += i
    decrypted_text = decrypted_text.replace("И  ", "Й ")
    return decrypted_text

def main():
    """

    """
    args = parse()
    config = open_json_file(args.config_1)
    key_1 = open_json_file(args.key_1_name)
    text = open_file(config["input_text"])
    output = encrypt(text, config["alphabet"], key_1["offset"])
    save_file(config["output_text"], output)
    config = open_json_file(args.config_2)
    text = open_file(config["encrypted_text"])
    #frequency_ru = open_json_file(args.frequency_ru)
    #frequency_text, key_2 = frequency_analysis(text, frequency_ru)
    #save_json_file(config["frequency_cod4"], frequency_text)
    #save_json_file(config["key_2"], key_2)
    key_2 = open_json_file(config["key_2"])
    decrypted_text = decrypt(text, key_2)
    save_file(config["decrypted_text"], decrypted_text)



if __name__ == "__main__":
    main()