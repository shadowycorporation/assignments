# Assignment 4

#### Value: 200 shadowcoins

#### Data files

* [code.txt](code.txt)

### Cracking codes

Our client has intercepted a top secret communication from a competitor! Unfortunately, the message
is encrypted. We have reason to believe, though, that the competitor did not use military-grade
encryption, but instead opted for a rather weak cipher called the
[Caesar cipher](https://en.wikipedia.org/wiki/Caesar_cipher).

### Caesar cipher

The Caesar cipher simply shifts each letter of the plaintext by a certain value, to obtain the
ciphertext. For example, if the shift value is 1, then

```
A -> B
B -> C
C -> D
...
X -> Y
Y -> Z
Z -> A
```

Note that Z wraps around and becomes A. If the shift value were two, then
```
A -> C
B -> D
C -> E
...
X -> Z
Y -> A
Z -> B
```
and so on.

We don't know by what value the competitor's message was shifted. But there aren't so many values
that we can't just try them all!

### Requirements

Write a program that shifts the message by all possible values and prints it out. Then, pick out
the correctly decrypted message and submit it with your code, and account number.

## Hints

### ASCII

Computers think about letters as if they were numbers. To do this, each letter has a special
numerical value. The encoding that allows computers to convert between letters and numbers is called
[ASCII](http://www.asciichart.com/).

Note that in the chart in the link above, there are 128 values (0-127). Some of those values encode
special, unprintable characters; some encode punctuation marks; and some encode the lower and upper
case letters, `a...z` and `A...Z`. You can convert any letter to its numerical ASCII value, and any
number 0-127 to its letter value, using the functions `ord()` and `chr()`, respectively. Examples:

```python
print(ord('a'))  # Prints 97
print(ord('A'))  # Prints 65
print(chr(98)    # Prints 'b'
print(chr(33))   # Prints '!'
print(chr(0))    # Prints nothing: 0 is the special null character.
```

Once a letter is converted to its ASCII value, you can perform math on it. For example:
```python
ascii_value = ord('a')  # Value = 97
ascii_value += 1        # Value = 98
print(chr(ascii_value)) # Prints 'b'
```

Viola, you have shifted the letter by 1.

But what if you shift 'z' by 1?

```python
ascii_value = ord('z')  # Value = 122
ascii_value += 1        # Value = 123
print(chr(ascii_value)) # Prints '{'
```

The ASCII value of 123 is the left curly brace '{' -- that's not what we want.
We *want* the letter 'a', which has the ASCII value 97. So, we must correct our math, and subtract
26 (since there are 26 letters in the alphabet):

```python
ascii_value = ord('z')  # Value = 122
ascii_value += 1        # Value = 123
if ascii_value > 122:   # Perform correction
    ascii_value -= 26
print(chr(ascii_value)) # Prints 'a'
```

Our Master Hacker started this function for you, but didn't finish. Fill it out to make it easy to
perform the shifting:

```python
def shift(letter, distance):
    ascii_value = ord(letter)
    if ascii_value >= 97 and ascii_value <= 122:  # Letter is lowercase, between 'a' and 'z'
        # TODO: shift letter, correct for wrap-around if needed

        new_letter = chr(ascii_value)
    elif ascii_value >= 65 and ascii_value <= 90: # Letter is uppercase, between 'A' and 'Z'
        # TODO: shift letter, correct for wrap-around if needed

        new_letter = chr(ascii_value)
    else:
        # The character is not a letter, but a number, space, or punctuation mark. These did not
        # get encrypted, so we don't decrypt them. Return them unchanged.
        new_letter = letter

    return new_letter
```

You can use this function in your code like this:

```python
letter = 'a'
distance = 5
shifted_letter = shift(letter, distance)
print(shifted_letter)
```

### Ranges

To test many shift distances quickly, you need a list of distances to shift by. You could create
this list by hand like this:

```python
distances = [1, 2, 3, 4, 5, 6 ... ]
```

but that's tedious: you have to write out all of the values by hand. Why not have the computer do
that for you? This is where the `range()` function comes in. It produces a list of values for you.
Note that you should provide two parameters, the starting and ending values. Note that there is a
caveat: the starting value is *included*, but the ending value is *excluded*:

```python
distances = list(range(1, 10))
print(distances)
```

Try the above code and see what is the list of ranges that it produces. Then modify it to be useful
for this assignment.


### Pretty printing

The Python `print()` function always prints a new line at the end of anything you print. Example:

```python
for letter in 'hello':
    print(letter)
```

results in
```
h
e
l
l
o
```

Not always what you want. To prevent this behavior, you can tell the `print()` function that instead
of a newline on the end, it should print something else. For example, you can tell it to print a
comma (`,`) after everything by using the `end` parameter:

```python
for letter in 'hello':
    print(letter, end=',')
```

results in

```
h,e,l,l,o,
```

Hm, better, but not quite that useful either. You can also tell `print()` to end with *nothing*, or
the "empty string" (`''` or `""`):

```python
for letter in 'hello':
    print(letter, end="")
```

results in

```
hello
```

Perfect! Well, almost: now multiple prints will follow each other with no line break. Example:

```python
for letter in 'hello':
    print(letter, end='')
for letter in 'there':
    print(letter, end='')
```

results in

```
hellothere
```

You can fix this, however, by adding an empty `print()` in between, like this:

```python
for letter in 'hello':
    print(letter, end='')

print()

for letter in 'there':
    print(letter, end='')
```

Result:

```
hello
there
```

