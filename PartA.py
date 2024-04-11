import sys
from collections import defaultdict
from collections import deque

class Token:

    def __init__(self):
        self.tokens = defaultdict(int)

    def tokenize(self, file: str):
        #function takes in a file object and then returns a list of tokens
        #the input paramters is a .txt file and is a string
        temp = deque()
        with open(file, "r") as f:
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
                                    self.tokens[word[:i]] += 1
                                temp.append(word[i+1:])
                                break
                            i += 1
                        else:
                            if word != "":
                                self.tokens[word] += 1
                        temp.popleft()

    def computeWordFrequencies(self):
        return self.tokens.items()


    def print(self):
        #function prints out the word frequencies

        sorted_word_count = dict(sorted(self.computeWordFrequencies(), key=lambda x: (-x[1], x[0])))

        for word, count in sorted_word_count.items():
            print(f"{word} {count}")


if __name__ == "__main__":
    test = Token()
    if len(sys.argv) <= 1:
        print("please input a file")
    else:
        for i in sys.argv[1:]:
            test.tokenize(i)
    test.print()
    print("made it this far")

