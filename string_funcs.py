"""
Module to provide a suite of String manipulation classes and functions.
"""

from itertools import permutations

class StringFuncs:
    """
    Represents a String object and a suite of String manipulation functions.
    """

    def __init__(self, string: str):
        self._string = string

    @property
    def string(self):
        """
        Getter method for object field _string.
        :return: value of _string
        """
        return self._string

    def remove_sub(self, substring: str) -> str:
        """
        Removes the first occurrence of SUBSTRING from existing String. No effect if SUBSTRING
        is not found.
        :param substring: string to be removed form existing string
        :return: Existing string with first occurrence, if any, of SUBSTRING removed.
        """
        i = self._string.find(substring)
        if i != -1:
            self._string = self._string[:i] + self._string[i + len(substring):]
        return self.string

    def append_string(self, string: str) -> str:
        """
        Adds STRING to the end of existing string.
        :param string: String to be added.
        :return: New concatenated string.
        """
        self._string += string
        return self.string

    @staticmethod
    def mirror_string(string: str) -> str:
        """
        Mirrors (reverses) String sequence.
        :param string: Input String to be mirrored.
        :return: Mirrored String
        """
        return string[::-1]

    @staticmethod
    def load_string(in_file: str) -> str:
        """
        Load file contents as a String.
        :param in_file: Filename to be read.
        :return: Contents of the file.
        """
        with open(in_file, 'r', encoding='utf-8') as stream:
            contents = stream.read()
        return contents

    @staticmethod
    def save_string(out_file: str, string: str) -> None:
        """
        Write String to a file.
        :param out_file: Name of file to be created and written to.
        :param string: String to be written.
        """
        with open(out_file, 'w', encoding='utf-8') as stream:
            stream.write(string)


class Anagram(StringFuncs):
    """
    A StringFuncs subclass with functions to test for and get Anagrams.
    """
    def is_anagram(self, string: str) -> bool:
        """
        Function to test whether STRING is an anagram of stored existing _string,
        irrespective of case.
        :param string: Input STRING to be tested.
        :return: Whether STRING is an anagram of _string.
        """

        # Consider identical strings to NOT be anagrams of one another. Ignore case.
        if string.lower() == self.string.lower():
            return False

        # First, check if both strings contain the same set of unique characters,
        # ignoring repetition.
        if set(string.lower()) != set(self.string.lower()):
            return False

        # Count number of repetitions of unique characters. STRING is an anagram the
        # existing _STRING iff number of repetitions of unique characters match. We
        # already know both strings contain the same set of unique characters
        lets1 = {}
        lets2 = {}
        for char in self.string.lower():
            lets1[char] = lets1.get(char, 0) + 1
        for char in string.lower():
            lets2[char] = lets2.get(char, 0) + 1

        for char in lets1.keys():
            if lets1.get(char) != lets2.get(char):
                return False

        return True

    def get_anagrams(self) -> set:
        """
        Function to get a set of all anagrams of _string.
        :return: Set of anagrams.
        """
        all_anagrams = set()
        for perm in permutations(self.string.lower()):
            word = ""
            for char in perm:
                word = word.join(char)
            all_anagrams.add(word)

        return all_anagrams


class Palindrome(StringFuncs):
    """
    A StringFuncs subclass that can only store Palindromic strings.
    """
    def __new__(cls, string):
        # If string is not a palindrome, do not create a new instance and
        # return None instead.
        if string.lower() != StringFuncs.mirror_string(string).lower():
            return None
        return object.__new__(cls)
