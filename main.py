from random import randint, sample, choice
import string
import unicodedata


class PasswordGenerator:

    def __init__(self, level: int, nb_chars_min: int = 0, nb_chars_max: int = 0):
        self.__level = level
        self.__nb_chars_min = nb_chars_min
        self.__nb_chars_max = nb_chars_max

    def __str__(self):
        return self.__generate_password()

    def __generate_password(self) -> str:
        strings_list = []

        match self.__level:
            case 1:
                strings_list = [self.__get_random_word()]
            case 2:
                strings_list = [self.__get_random_word()] + self.__get_random_ascii_lowercase_chars(1) + \
                               self.__get_random_ascii_uppercase_chars(1) + self.__get_random_digits(1) + \
                               self.__get_random_punctuation_chars(1)
            case 3:
                strings_list = [self.__get_random_word()] + self.__get_random_ascii_lowercase_chars(3) + \
                               self.__get_random_ascii_uppercase_chars(3) + self.__get_random_digits(3) + \
                               self.__get_random_punctuation_chars(3)
            case 4:
                strings_list = list(string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation)
            case 5:
                strings_list = self.__get_unicode_chars()

        string_list_length = len(strings_list)
        if self.__nb_chars_max:
            if self.__nb_chars_max > string_list_length:
                return ""
            string_list_length = randint(self.__nb_chars_min, self.__nb_chars_max)

        strings_list = "".join(sample(strings_list, string_list_length))

        return strings_list

    @staticmethod
    def __get_unicode_chars() -> list[str]:
        unicode_chars = []

        for code in range(0, 1500):
            try:
                # la ligne suivante sert juste à lever une ValueError s'il n'y a pas de name
                # le code ne sera donc pas ajouté à la liste
                name = unicodedata.name(chr(code))
                str_chr_code = str(chr(code)).strip()
                if str_chr_code != "":
                    unicode_chars.append(str_chr_code)
            except ValueError:
                pass

        return unicode_chars

    @staticmethod
    def __get_random_ascii_lowercase_chars(nb: int) -> list[str]:
        return [choice(string.ascii_lowercase) for _ in range(nb)]

    @staticmethod
    def __get_random_ascii_uppercase_chars(nb: int) -> list[str]:
        return [choice(string.ascii_uppercase) for _ in range(nb)]

    @staticmethod
    def __get_random_digits(nb: int) -> list[str]:
        return [choice(string.digits) for _ in range(nb)]

    @staticmethod
    def __get_random_punctuation_chars(nb: int) -> list[str]:
        return [choice(string.punctuation) for _ in range(nb)]

    @staticmethod
    def __get_random_word() -> str:
        with open("mots.txt", "r", encoding="utf8") as file:
            return choice(file.read().split())


if __name__ == '__main__':
    print(PasswordGenerator(level=1))
    print(PasswordGenerator(level=2))
    print(PasswordGenerator(level=3))
    print(PasswordGenerator(level=4, nb_chars_min=16, nb_chars_max=32))
    print(PasswordGenerator(level=5, nb_chars_min=64, nb_chars_max=128))
