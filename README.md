# cs121-a1

# Assignment 1: Text Processing
## Terry Kim - 56288781
## Part A: Word Frequencies

### Class: Token()

This class contains the methods for tokenizing, printing, and computing. It has an attribute self.tokens which is a defaultdict structure that stores all the unique words as keys
and the value is the number of occurrences of that word. 

### Method: tokenize(self, file: str):

This method reads in a text file and does not return anything but instead modifies the self.tokens attribute in place. It goes through each line of the file and then each individual character and will determine if the word is valid or not and then update the dictionary as needed. Runs in O(n)

### Method: computeWordFrequencies(self):

This method counts the number of occurrences of each unique token in the dictionary. Takes O(1) to return the number of keys in the dictionary.

### Method: print(self):

This method prints the <token> <freq>. Runs in O(nlogn) because we are sorting the dictionary by decreasing frequency and alphabetically if tied.

### Running the Program

If an input file is not specified it will return an error.

If one file is given then it will return the printed <token> <freq> and it will also return the number of occurrences of each token.

If multiple files are given, then it will accumulate all the unique words for each of the files and will print the combined <token> <freq> as well as the combined number of occurrences of each token.

## Part B: Intersection of Two Files

### Class: Intersection(Token)

This class inherits from the Token Class that was previously written for Part B.

### Method: process(self, word: str) 

This method returns True if the word is already present in the self.tokens class attribute else it will return False. Takes O(1) time to do a key lookup in the dict

### Method: intersect(self, file1: str, file2: str)

This method reads in two files at a time and returns the number of words in common between the two. Runs in O(n+m) time

### Running the Program

If an input file is not specified it will return an error.

If one file is given then it will return the error to provide an additional file.

If multiple files are given, then it will accumulate all the unique words for each of the files in pairs and will print the combined number of common words between them. If there are an odd number of files given then the last one will not be processed because it doesn't have a pair.

Valid:
python PartB.py file1 file2 file3 file4

Not Valid:
python PartB.py file1 file2 file3

file 3 will not be processed
