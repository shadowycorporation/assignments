# Assignment 2

#### Value: 100 shadowcoins

### Genetic sequencing

A client of Shadowy Corporation, Inc, is developing a prototype mutant. This is a top secret
project, and may not be shared with anyone. The mutant is a biological lifeform with DNA similar to
a human, but with significant mutations that give it the powers being researched.

The client requires a sequencing of some sections of the mutatant's DNA.

### DNA

DNA sequences consist of 4 letters, each letter encoding a specific amino acid. For example, here is
a sample of DNA:

```
AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC
```

It consists of the symbols `A, C, G, and T`.

### Requirements

The client requires you to write a program to count the number of each type of symbol in the DNA.
There is a file provided with this assignment, [mutant_dna.txt](mutant_dna.txt), which has a section
of DNA of interest to the client. Your assignment is to count all of the DNA symbols.
Make sure you either download, or copy the file, into your PyCharm project. It must be present in
order for your code to have access to it!

### Reading files

Master Hackers at Shadowy Corp. are providing you with some code to get started. Make sure that you
copy the entire mutant DNA file, and add it to your PyCharm project. Then, try running the following
code to get started:

```python
# Let's open the mutant dna file. This is how it's done in Python:
with open('mutant_dna.txt') as dna_file:
    # Now, we will traverse each symbol in the file, one at a time:
    for symbol in dna_file.read():
        print(symbol)  # This just prints out each symbol. This is debugging purposes only.

# Outside of the `with` statement, the file has already been closed. The following statement would
# result in an error, if you were to uncomment it and run it:
#print(dna_file.read())
```

### Hints

* To understand what is happening in the `for` loop above, refer to
  [this tutorial on for loops](https://www.tutorialspoint.com/python/python_for_loop.htm).
  A `for` loop simply goes through each item in a list of items. For example:
```python
for letter in 'abcdefg':
    print(letter)

for number in [1, 2, 3, 4, 5]:
    print(number)
```
  This would just go through each letter or number, respectively, in the lists above, and print each one.
  In the case of the assignment, the statement `dna_file.read()` produces a list of all of the
  letters in the file. The `for` loop then goes through all of them.
  `for` loops work for on all lists and list-like objects. See the tutorial for more examples.
* In the previous assignments, you compared numbers (eg. `while n < 1000`). For comparing *words* or
  *letters*, you must surround them with single or double quotes. Eg.
```python
if name == 'hacker':
  do_something()

# OR
if name == "hacker":
  do_something()
```
  Refer to [this tutorial](https://www.tutorialspoint.com/python/python_if_else.htm) for more info
  on `if` statements.
* You will also need to create some variables to store the counts of each symbol, and increment
  these variables when the appropriate symbol is observed.
* Don't forget to print out and submit the final counts of each of your variables!
  A useful way to print things is to use formatting to insert values into the things you want to print:
```python
hacker = 'hacker 7'
print(f'Hello, {hacker}')
# Prints: 'Hello, hacker 7'

age = 11
print(f'I am {age} years old')
# Prints: 'I am 11 years old'
```
  Make sure you define your variables beforehand, and then prefix your output string with `f`, to
  tell Python that it is a special string that should be formatted.

Good luck, and happy hacking.

