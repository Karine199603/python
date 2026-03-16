import random
import string


def generate_str(
    length: int,
    digits: int = 0,
    symbols: int = 0,
    lowercase: bool = False,
    uppercase: bool = False,
    cyrillic: bool = False
) -> str:
    """
    Generate a random string with optional digits, symbols, and alphabet settings.

    The function creates a random string of a given length
    using either the Latin or Cyrillic alphabet,
    optionally include a specified number of digits and punctuation symbols,
    which will replace random characters in the string.

    :param length: Total length of the generated string.
    :param symbols: Number of punctuation symbols to include. Default is 0.
    :param digits: Number of digits (0–9) to include in the string. Default is 0.
    :param lowercase: If True, use only lowercase letters. Default is False.
    :param uppercase: If True, use only uppercase letters. Default is False.
    :param cyrillic: If True, use the Cyrillic alphabet. Default is False.
    :return: A randomly generated string.
    """

    cyrillic_alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

    if not cyrillic:
        if lowercase:
            alphabet = string.ascii_lowercase
        elif uppercase:
            alphabet = string.ascii_uppercase
        else:
            alphabet = string.ascii_letters
    else:
        if lowercase:
            alphabet = cyrillic_alphabet
        elif uppercase:
            alphabet = cyrillic_alphabet.upper()
        else:
            alphabet = cyrillic_alphabet + cyrillic_alphabet.upper()

    result = [random.choice(alphabet) for i in range(length)]

    if digits or symbols:
        if digits + symbols > length:
            return "The number of characters and digits exceeds the length of the string"
        else:
            available_indices = list(range(length))
            for i in range(digits):
                index = random.choice(available_indices)
                number = str(random.randint(0, 9))
                result[index] = number
                available_indices.remove(index)
            for i in range(symbols):
                index = random.choice(available_indices)
                symbol = random.choice(string.punctuation)      # symbols: #!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
                result[index] = symbol
                available_indices.remove(index)

    return "".join(result)


if __name__ == "__main__":
    print(generate_str(8))
