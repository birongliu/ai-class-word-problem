import random

class Dictionary:
    """
    Handles word lookups and random word selection for word transformations.
    """
    def __init__(self, dict_file_name=""):
        """
        Initializes the dictionary by reading words from a file.

        Args:
            dict_file_name (str): The name of the dictionary file.
        """
        self.file_name = dict_file_name
        self.word_dict = set()
        self.word_array = []
        
        if self.file_name:
            try:
                with open(self.file_name, "r") as dict_file:
                    print(">>...")
                    print("Reading dictionary...")
                    for line in dict_file:
                        word = line.strip().lower()
                        self.word_dict.add(word)
                        self.word_array.append(word)
                print("Dictionary Initialized...")
                print("...<<")
            except FileNotFoundError as e:
                print(f"Error: Could not open file {self.file_name}")
                print(f"Error: {e}")

    def search_word(self, word):
        """
        Checks if a word exists in the dictionary.

        Args:
            word (str): The word to search for.

        Returns:
            bool: True if the word is found, False otherwise.
        """
        return word in self.word_dict

    def get_words(self, word_length):
        """
        Retrieves two random words of a specified length from the dictionary.

        Args:
            word_length (int): The length of words to retrieve.

        Returns:
            list: A list containing two words of the specified length, or an empty list if none are found.
        """
        words = [word for word in self.word_array if len(word) == word_length]
        if len(words) < 2:
            return []
        return random.sample(words, 2)
