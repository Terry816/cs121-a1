# cs121-a1

Tokenizer and Word Frequency Counter
Part A: Word Frequencies
Method/Function: List<Token> tokenize(TextFilePath)
This method/function reads in a text file and returns a list of tokens in that file. Tokens are sequences of alphanumeric characters, independent of capitalization (e.g., "Apple", "apple", "aPpLe" are the same token). Regular expressions and external tokenizers (e.g., NLTK) are not allowed.

Method/Function: Map<Token,Count> computeWordFrequencies(List<Token>)
This method/function counts the number of occurrences of each token in the token list. It should be implemented without using the Counter class or similar libraries.

Method/Function: void print(Frequencies<Token, Count>)
This method/function prints out the word frequency count onto the screen. The printout should be ordered by decreasing frequency, with ties broken alphabetically.

Running the Program
Your program must run from the command line, taking one text file as an argument and outputting the token frequencies.
