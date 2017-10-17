# Assignment 3

#### Value: 200 shadowcoins

### Beware of clients

Shadowy Corporation, Inc, contracts with many clients. Some of them are ... less than honest.
Shadowy Corp. has recently fullfilled a contract for a client, who has refused to pay for services.
Luckily, Shadowy Corp. has other means of getting paid.

### Cryptographic hashing

We have acquired the password to the client's bank account. We intend to extra the payment due to us
and not a penny more (we are Shadowy, but we are Honest after all!).

```
password = '5ed728c2fa5d767bc6c1ec6a732db1e37c343be46913e6498d340f7782691f14'
```

Unfortunately, this is not the actual password string. This password is hashed using the
[SHA-256 hashing algorithm](https://en.wikipedia.org/wiki/SHA-2).
Hashing is a way to transform an input string into gibberish in a way that is impossible to reverse.

For example, hashing the values on the left using the `sha256` function *always* produces the values
on the right:
```
sha256('hi there') = '9b96a1fe1d548cbbc960cc6a0286668fd74a763667b06366fb2324269fcabaa4'
sha256('asdf') = 'f0e4c2f76c58916ec258f246851bea091d14d4247a2fc3e18694461b1816e13b'
sha256('I am a banana') = '1b03698eebabf86b80bbf6745d5a786912c979e2983160f0af18a42058e061e6'
```

Note three important things about hashing algorithms:

1. An input will *always* produce the same output when hashed.
2. An input will *never* produce the same output as another input when hashed (this is not
   completely true, but the chances that two inputs produce the same output (called "collision")
   are smaller than the chances of the Earth being destroyed in the next 5 seconds.
   1...2...3...4...5... ...)
3. It is pretty much impossible to reverse a hash into its original input.

Knowing these things, how would we go about figuring out the password?

### Cracking passwords

Shadowy Corporation knows that this client is using a simple
