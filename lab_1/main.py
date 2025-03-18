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

def main():
    """
    Handle argument parsing and execute
    """
    args = parse()
    config = open_json_file(args.config_1)
    key_1 = open_json_file(args.key_1_name)
    text = open_file(config["input_text"])
    output = encrypt(text, config["alphabet"], key_1["offset"])
    save_file(config["output_text"], output)


if __name__ == "__main__":
    main()