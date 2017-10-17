# Assignment 3

#### Value: 200 shadowcoins

### Song lyrics

Our client has created a hit song, [the Name Game](https://en.wikipedia.org/wiki/The_Name_Game).
Shadowy Corporation doesn't know why this song is such a hit -- but it is, and there is money to be
made, and you will receive a share of it if you choose to help with this assignment.

This song is so silly, it shouldn't even be allowed. But it's popular, so we must work with what
we've got. You can listen to the song here: [the Name Game](https://www.youtube.com/watch?v=5MJLi5_dyn0).

The song's lyrics simply take a name, and replace the name with a "funny" change, like this:

```
Katie, Katie, bo-batie,
Banana-fana fo-fatie,
Fee-fy-mo-matie,
Katie!

Tony, Tony, bo-bony,
Banana-fana fo-fony,
Fee-fy-mo-mony,
Tony!
```

In the first line, after repeating the name twice, you drop the first letter of the name and replace
it with a `b`.
In the second line, drop the first letter and replace it with an `f`.
In the third line, drop the first letter and replace it with an `m`.
Finally, print out the name followed by an exclamation on the fourth line.

Pretty simple, eh?

### Requirements

Write a program that takes a name as input, and produces the lyrics for this song. You don't need to
submit any output for this assignment, just the code. And of course, your account number.

## Hints

### User input

This program should ask the user for their name. You can ask the user to enter information like this:

```python
user_input = input('Please say "hi": ')
if user_input == 'hi':
    print('Well hello there!')
else:
    print(f'You did not say "hi". You did not say "hi" at all. You said "{user_input}". You suck.')
```
Try running this code and entering different things at the prompt, to see how it works.

### String slices

Strings are just lists of letters, and all lists in Python can be "indexed" and "sliced".

Indexing means to take an item at a certain position in the list. Example:

```python
# This is a list of fruit.
fruit = ['apple', 'banana', 'mango', 'peach']

# Take the 1st item in the list (the 1st item is at position 0; this is a rule in Python
# and many other programming languages, but not all of them).
print(fruit[0])

# Take the 3rd item in the list (the 3rd item is at position 2; in general, the nth item is always
# at position n-1).
print(fruit[2])

# Take the last item in the list:
print(fruit[-1])

# Take the second-to-last item in the list:
print(fruit[-2])

# Strings are just lists of letters:
word = 'monkey'

# Take the 4th letter
print(word[3])

# Take the 17th letter
print(word[16])
# Uh oh, what happened here? 'monkey' doesn't have 17 letters, so there's a problem if you try to
# index this list on a position that is out of bounds.
```

Slicing means to take a range of values from a list. The first value in a slice is the first index
to take (inclusive), and the second value in a slice is the *number* of items to take. Example:

```python
fruit = ['apple', 'banana', 'mango', 'peach']

# Starting with the 1st item, take two total.
print(fruit[0:2])

# Starting with the 3rd item, take the rest of the items to the end.
print(fruit[2:])

word = 'monkey'

# Get 'key' from 'monkey'
print(word[3:])
```

Please take a moment to run the above code, it's very important that you understand how lists work.
Here is more information on [lists](https://www.tutorialspoint.com/python/python_lists.htm)
and [strings](https://www.tutorialspoint.com/python/python_strings.htm).

### String concatenation

Since you can slice lists and strings, you can also combine them, simply by using the `+` operator.
For example:

```python
word = 'monkey'

# Get 'money' from 'monkey'
word1 = word[0:3]  # Get first three letters
word2 = word[4:]   # Get all letters from index 4 to the end
print(word1 + word2)  # Combine the two snippets
```

## Bonuses

### Bonus 1

#### Value: 50 shadowcoins

The song's lyrics usually remove the first letter of the name, and replace it with one of
`b, f, or m`. However, what happens if a person has a name that starts with a vowel?

```
Arthur Arthur bo-brthur,
Banana-fana-fo-frthur,
...
```

Eww, that's pretty bad. It's hard to sing! This'll never work. You can earn this bonus if you check
that a name starts with a vowel, and in that case, *don't* drop the first letter. So, for poor
Arthur, that would be

```
Arthur Arthur bo-barthur,
Banana-fana-fo-farthur,
...
```

### Bonus 2

#### Value: 50 shadowcoins

According to the rules of the song, if the name starts with one of the replacement letters, you
should drop the first letter, but then *don't* replace it. Example with Bob:

```
Bob Bob bo-ob,
Banana-fana-fo-fob,
Fee-fy-mo-mob,
Bob!
```

Example with Mary:

```
Mary Mary bo-bary,
Banana-fana-fo-fary,
Fee-fy-mo-ary,
Mary!
```

### Bonus 3

#### Value: 50 shadowcoins

Some people have names that start with two letters that make one sound. For example, Charlie. For
these names, you should drop both first letters. Example:

```
Charlie Charlie bo-barlie,
Banana-fana-fo-farlie,
Fee-fy-mo-marlie,
Charlie!
```

### Bonus 4

#### Value: 50 shadowcoins

This is a family-friendly song. However, some people will try to make the lyrics into something
bad in order to ruin the reputation of our client. For example, someone might enter then name
"Jutt". What happens then is terrible!

```
Jutt Jutt bo-****
...
```

That is unacceptable. The client will not tolerate Mommy-No-No's in the song lyrics.
Please add a check to the beginning of the program that ensures that names entered by the user
cannot be used to create inappropriate lyrics. If a user does enter such a name, print out
"We do not tolerate such lyrics in our song. The authorities have been notified."

Then, run the following code to terminate the program:
```python
import sys
sys.exit()
```
All this does it tell your program to import some additional functions from `sys`, and then to
exit early, without executing any of the rest of your code.

