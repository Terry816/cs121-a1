from PartA import Token
import sys
from collections import deque


class Intersection(Token):

    def __init__(self):
        Token.__init__(self)
        self.num_intersect = 0


    #Runtime Complexity: O(1) because dictionary lookups are constant
    def process(self, word: str):
        return True if word in self.tokens else False


#Runtime Complexity: O(n+m). "n" is the total length of the first file. "m" is the total length of the second file.
#The function first calls the tokenize method inherited from it's child class that I wrote in Part A. We know that the runtime complexity for that function
#is O(n) and will run in linear time. In this new function we copied the main logic for the tokenize functions except now for each valid word that we find
# in the second file, we want to call the process function which returns True or False depending if the word was present in the first file. 
#We are going to do this for the entirety of the second file so it will take O(m) time.
#However, since we are checking each of the elements in the second file with the first file, it would take O(n+m) time total.

    def intersect(self, file1: str, file2: str):
        seen = set() # we do not need to repeatedly process a word we have seen already like "the, "a", "and" so before we call the process method we  
                    # want to add it to set which has O(1) lookup, to reduce the time for checking all the repetitive words in self.tokens
        self.tokenize(file1) #calling this inherited method is O(n).
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
        self.num_intersect += res
        return res
        
    def amount_intersect(self):
        return self.num_intersect

if __name__ == "__main__":
    test = Intersection()

    if len(sys.argv) <= 1:
        print("Please input a file")
    elif len(sys.argv) <= 2:
        print("Please provide file paths in pairs (e.g., python script.py file1 file2 file3 file4)")
    else:
        for i in range(1, len(sys.argv), 2):
            if i + 1 < len(sys.argv):
                file1 = sys.argv[i]
                file2 = sys.argv[i + 1]
                print(test.intersect(file1, file2))
            
