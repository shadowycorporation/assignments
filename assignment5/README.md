# Assignment 5

#### Value: 200 shadowcoins

### Gaming the system

One of our clients is a game designer in the video gaming industry. He has come up with a game
that may prove to *so* great, and *so* popular, and *so* fun, that anyone still playing
Heroes Charge will instantly quit that game, and come play our client's game instead.

Unfortunately for our client, but fortunately for Shadowy Corporation, Inc, and for you, the client
is not a hacker and cannot write the game himself. He has contracted Shadowy Corp. for our team of
elite hackers to write the game instead.

### Requirements

The game is as simple as it is genius. Here's how it works:

* The program picks a secret number between 1 and 100
* The program prompts the user to make a guess at the secret number
* If the user's guess is correct, the game ends: the user has won! The program informs the user of
  this and prints out the number of guesses taken.
* If the user's guess is too high or too low, the program informs the user which one, and the user
  may continue guessing.
* If the user exceeds 10 guesses, the game ends: the user has lost! The program informs the user of
  this and prints our the secret number.

You do not need to submit any output for this assignment, only the code and your account number.

## Hints

### Random numbers

Python can easily generate random numbers. To do this, import the `random` module at the top of your
program. Then you can use the [`random.randint(a, b)`](https://docs.python.org/3/library/random.html#random.randint)
function to get a random integer between `a` and `b` (inclusive). Example:

```python
import random

n = random.randint(1, 10)  # n is now an unknown random integer such that 1 <= n <= 10.
print(n)                   # Find out what n is.
```

### Infinite loops

You've learned to write `while` loops that repeat while a certain condition is true, and end when it
becomes false. But sometimes it's useful to run a loop *forever*:

```python
while True:
    print('INFINITY')
```

Be careful running the above code! It will repeat *forever* (or at least until your computer blows
up, or you force-stop it using the Stop button in PyCharm).

Infinite loops can still be ended by the program, though, when it is convenient to do so. This is
accomplished using the `break` statement. For example:

```python
while True:
    # Annoy the user forever.
    word = input("What's the magic word? ")

    if word == 'please':
        # Ok, user said please, let's stop annoying them.
        break
```

Note the use of the statement `break`: this will cause the program to exit from the loop. But if the
user never says the right word, the loop will continue over, and over, and over, and over...

Please keep in mind that infinte loops are *usually* bad: it often means that you've forgotten to
update the condition that will make the loop exit.
See [the section on infinite loops here](https://www.tutorialspoint.com/python/python_while_loop.htm)
for an example.

In the case of the number-guessing-game, however, we are using the infinite loop in a controlled way
to allow the user to keep guessing, and only break out of it when the game ends.

