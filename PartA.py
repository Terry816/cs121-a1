import sys
from collections import defaultdict


class Token:

    def __init__(self):
        self.tokens = defaultdict(int)


    def tokenize(self, file: str):
        #function takes in a file object and then returns a list of tokens
        #the input paramters is a .txt file and is a string

        with open(file, 'r') as file:
            for line in file:
                for word in line.strip():
                    if word.isalnum():
                        self.tokens[word.lower()] += 1

    def computeWordFrequencies(self):
        return self.tokens.items()


    def token_print(self):
        #function prints out the word frequencies

        s = self.computeWordFrequencies()

        return s.sort(key = lambda x: (-x[1], x[0]))


