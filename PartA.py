import sys
from collections import defaultdict, deque

class Token:

    def __init__(self):
        self.tokens = defaultdict(int)

#tokenize function: Runtime Complexity is O(n). "n" is the total length of the file or the length of every single character in the input file.
#The function parses through each letter of the input file and checks whether the ascii value of the character is valid within the selected ranges (a-z) and (0-9).
#if there are special characters inside words, then it will split the word wherever the special character is. i.e. Ad@m - > { ad: 1, m :1}
#It will run in linear time relative to the size of the input.
    def tokenize(self, file: str):
        temp = deque()
        with open(file, "r", encoding="utf-8") as f:
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

#computeWordFrequencies function: Runtime Complexity is O(1) because hashmap lookup is constant and stored in memory.
    def computeWordFrequencies(self):
        return len(self.tokens)


#print function: Runtime Complexity is O(n log n). "n" is the total length of the keys in the dictionary.
#Although iterating in the for loop is just O(n), the sorting algorithm takes O(nlogn) time to run.
    def print(self):
        #function prints out the word frequencies

        sorted_word_count = dict(sorted(self.tokens.items(), key=lambda x: (-x[1], x[0])))

        for word, count in sorted_word_count.items():
            print(f"{word} {count}")


if __name__ == "__main__":
    test = Token()

    #We are calling the tokenize function k times, with k being the number of input files.

    if len(sys.argv) <= 1:
        print("please input a file")
    else:
        for i in sys.argv[1:]:
            test.tokenize(i)
    test.print()
    print(f"this is the number of occurences of each token: {test.computeWordFrequencies()}")
    print("Done with the test cases \n")


