# cs121-a1

# Tokenizer and Word Frequency Counter

## Part A: Word Frequencies

### Method/Function: `List<Token> tokenize(TextFilePath)`

This method/function reads in a text file and returns a list of tokens in that file. Tokens are sequences of alphanumeric characters, independent of capitalization (e.g., "Apple", "apple", "aPpLe" are the same token). Regular expressions and external tokenizers (e.g., NLTK) are not allowed.

### Method/Function: `Map<Token,Count> computeWordFrequencies(List<Token>)`

This method/function counts the number of occurrences of each token in the token list. It should be implemented without using the `Counter` class or similar libraries.

### Method/Function: `void print(Frequencies<Token, Count>)`

This method/function prints out the word frequency count onto the screen. The printout should be ordered by decreasing frequency, with ties broken alphabetically.

### Running the Program

Your program must run from the command line, taking one text file as an argument and outputting the token frequencies.

Example output formats:

- `<token>\t<freq>`
- `<token> <freq>`
- `<token> - <freq>`
- `<token> = <freq>`
- `<token> > <freq>`
- `<token> -> <freq>`
- `<token> => <freq>`

## Part B: Intersection of Two Files

Write a program that takes two text files from the command line as arguments and outputs the number of tokens they have in common.

### Program Requirements

- The program should reuse the code written for Part A to tokenize and count the tokens.
- It should avoid reading the entire files into computer RAM, as some files may be very large.
- Programs that perform better will be given more credit than those that perform poorly.

