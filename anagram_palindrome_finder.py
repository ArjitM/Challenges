"""
Module to download a webpage and find all Palindromes or
Anagrams present.
"""
import sys
from urllib import request
from html.parser import HTMLParser
import re
from string_funcs import Palindrome, Anagram

class CustomParse(HTMLParser):
    """
    Subclass of HTMLParser to process HTML text
    and handle parsed data.
    """

    def __init__(self):
        super().__init__()
        self._words = []
        self._retain = False

    @property
    def words(self):
        """
        Getter method for parsed text.
        :return: Words that have been parsed.
        """
        return self._words

    def handle_data(self, data: str) -> None:
        """
        Method to specify how to handle data parsed.
        :param data: Data extracted from HTML input.
        :return:
        """
        if isinstance(data, str) and self._retain:
            data = data.strip()
            if data:
                data_list = data.split()
                self._words.extend(data_list)

    def handle_starttag(self, tag: str, attrs) -> None:
        """
        Method to specify how to handle HTML start tags.
        :param tag: Tag to handle.
        :param attrs: Additional attributes (not used).
        :return:
        """
        if re.match("h[0-9]*", tag) or tag in {'p', 'code', 'li'}:
            self._retain = True

    def handle_endtag(self, tag: str) -> None:
        """
        Method to specify how to handle HTML end tags.
        :param tag: Tag to handle.
        :return:
        """
        if re.match("h[0-9]*", tag) or tag in {'p', 'code', 'li'}:
            self._retain = False


if __name__ == '__main__':
    url = sys.argv[1]

    with request.urlopen(url) as page_source:
        # Extract page source as a string and decode.
        html = page_source.read().decode('utf-8')

    # Use parser to parse through HTML input.
    parser_instance = CustomParse()
    parser_instance.feed(html)

    # Get parsed words and remove duplicates
    unique_words = set(parser_instance.words)
    palindromes = []
    anagram_pairs = set()

    for word in unique_words:

        # If word is not a palindrome, p_obj will be None
        p_obj = Palindrome(word)
        if p_obj:
            palindromes.append(p_obj)

        word_obj = Anagram(word)
        for other_word in unique_words:
            if word_obj.is_anagram(other_word):
                # Add anagram pairs sorted in lexicographic order
                # to avoid duplicates.
                if word < other_word:
                    anagram_pairs.add((word.lower(), other_word.lower()))
                else:
                    anagram_pairs.add((other_word.lower(), word.lower()))

    print("==================Palindromes==================")
    for p_obj in palindromes:
        print(p_obj.string)
    print("==================Anagrams==================")
    for anagram_pair in anagram_pairs:
        print(anagram_pair)
