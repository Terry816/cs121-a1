from PartA import Token
import sys
from collections import defaultdict, deque

class Intersection(Token):

    def __init__(self):
        Token.__init__(self)

    def process(self, word: str):
        return True if word in self.tokens else False

    def intersect(self, file1: str, file2: str):
        seen = set() # we do not need to repeatedly process a word in the seen already like "the" "a" so before we check in the tokens we 
                    # want to add it to set of the seen variables to reduce the time for checking all the words in tokens
        self.tokenize(file1)
        res = 0
        temp = deque()
        with open(file2, "r") as f:
            for line in f:
                for word in line.strip().split():
                    temp.clear()
                    temp.append(word)
                    while temp:
                        word = temp[0].lower()
                        i = 0
                        while i < len(word):
                            letter = word[i]
                            if not ((ord(letter) >= 48 and ord(letter) <= 57) or \
                                (ord(letter) >= 97 and ord(letter) <= 122)):
                                if word[:i] != "":
                                    if word[:i] not in seen:
                                        seen.add(word[:i])
                                        if self.process(word[:i]):
                                            res += 1
                                temp.append(word[i+1:])
                                break
                            i += 1
                        else:
                            if word != "":
                                if word not in seen:
                                    seen.add(word)
                                    if self.process(word):
                                        res += 1
                        temp.popleft()

        self.tokens.clear()

        return res
        