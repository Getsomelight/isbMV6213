import json
import argparse
import math
from scipy.special import gammaincc


def parse() -> argparse.Namespace:
    """
    Handle argument parsing and return them
    Raises SyntaxError if no filenames is provided
    """
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("config", type=str)
        return parser.parse_args()
    except:
        raise SyntaxError("Path is empty")


def open_json_file(name: str) -> dict:
    """
    Open and read the content of the JSON file
    Raises FileNotFoundError if the JSON file cannot be found
    """
    try:
        with open(name, "r", encoding="UTF-8") as file:
            return json.load(file)
    except:
        raise FileNotFoundError("File doesnt found or doesnt exist")


def save_file(path: str, output: str) -> None:
    """
    Open and write the output file
    Raises Exception if the file cannot be found
    """
    try:
        with open(path, "w", encoding="UTF-8") as file:
            file.write(output)
    except:
        raise Exception("Cannot create output file")


def frequency_bitwise(sequence: list) -> float:
    """
    A NIST test for frequency bitwise of ones
    """
    s = 0
    for i in sequence:
        s += 1 if i == 1 else -1
    c = s / math.sqrt(len(sequence))
    return math.erfc(abs(c) / math.sqrt(2))


def identical_consecutive_bits(sequence: list) -> float:
    """
    A NIST test for identical consecutive bits
    """
    ratio = sum(sequence) / len(sequence)
    if not abs(ratio - 0.5) < 2 / math.sqrt(len(sequence)):
        return 0
    s = 0
    for i in range(len(sequence) - 1):
        s += 1 if sequence[i] != sequence[i + 1] else 0
    a = abs(s - 2 * len(sequence) * ratio * (1 - ratio))
    b = 2 * math.sqrt(2 * len(sequence) * ratio * (1 - ratio))
    return math.erfc(a / b)


def longest_sequence(sequence: list, block: int, pi: list) -> float:
    """
    A NIST test for longest sequences in blocks of sequence
    """
    block_max = [0, 0, 0, 0]
    for block_s in range(0, len(sequence), block):
        max_ones = 0
        block_e = block_s + block
        i = block_s
        while i < block_e:
            cur = 0
            while i < block_e and sequence[i] == 1:
                cur += 1
                i += 1
            i += 1
            max_ones = cur if cur > max_ones else max_ones
        match max_ones:
            case 0 | 1:
                block_max[0] += 1
            case 2:
                block_max[1] += 1
            case 3:
                block_max[2] += 1
            case _:
                block_max[3] += 1
    x = 0
    for i in range(4):
        x += (block_max[i] - 16 * pi[i]) ** 2 / (16 * pi[i])
    x = x**2
    return gammaincc(1.5, x / 2)


def main():
    """
    Provides operates to make a NIST test on random sequence of bits
    """
    args = parse()
    config = open_json_file(args.config)
    java_sequence = list(int(x) for x in config["Java"])
    cpp_sequence = list(int(x) for x in config["C++"])
    pi = config["pi"]
    block = config["block"]
    java = (
        "Java\nFrequency bitwise test: "
        + str(frequency_bitwise(java_sequence))
        + "\nIdentical consecutive bits test: "
        + str(identical_consecutive_bits(java_sequence))
        + "\nLongest sequence test: "
        + str(longest_sequence(java_sequence, block, pi))
    )
    cpp = (
        "C++\nFrequency bitwise test: "
        + str(frequency_bitwise(cpp_sequence))
        + "\nIdentical consecutive bits test: "
        + str(identical_consecutive_bits(cpp_sequence))
        + "\nLongest sequence test: "
        + str(longest_sequence(cpp_sequence, block, pi))
    )
    output = java + "\n\n" + cpp
    save_file(
        config["output"], output
    )


if __name__ == "__main__":
    main()
