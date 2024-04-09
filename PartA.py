import sys
from collections import defaultdict
from collections import deque

class Token:

    def __init__(self):
        self.tokens = defaultdict(int)


    def tokenize(self, file: str):
        #function takes in a file object and then returns a list of tokens
        #the input paramters is a .txt file and is a string

        for line in sys.stdin:
            for word in line.strip().split():
                temp = deque()
                temp.append(word)
                while temp:
                    word = temp[0]
                    i = 0
                    while i < len(word):
                        letter = word[i]
                        if not letter.isalnum():
                            self.tokens[word[:i]] += 1
                            temp.append(word[i+1:])
                            break
                        i += 1
                    else:
                        if word != "":
                            self.tokens[word.lower()] += 1
                    temp.popleft()
                    


    def computeWordFrequencies(self):
        return self.tokens.items()


    def tprint(self):
        #function prints out the word frequencies

        sorted_word_count = dict(sorted(self.computeWordFrequencies(), key=lambda x: (-x[1], x[0])))

        for word, count in sorted_word_count.items():
            print(f"{word}: {count}")


if __name__ == "__main__":
    print("hello")
    test = Token()
    test.tokenize("testA.txt")
    test.tprint()
    print("made it this far")


