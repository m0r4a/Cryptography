# AFFINE Encryption and Decryption

The AFFINE encryption method is the first encryption method I had to learn for my cryptography class. I like to think of it in the following way:

## Step 1: Variables

First, we have the variables. Specifically, for the purpose of the course, we use 5 variables:

- n: the alphabet size
- a: the first part of the encryption key
- b: the second part of the encryption key
- bs: the block size
- N: the alphabet size ** the block size used for the modulo operation if we're using higher block sizes than 1

In addition to, of course, the string we want to encrypt.

## Step 2: Letters to Numbers

With the variables defined, the next step in the encryption methods of my first cryptography exam is to convert the letters or text string into numbers to operate on them.

## Encryption

### Step 3: Encryption

The encryption process for the AFFINE cipher is as follows:

P = plaintext
E = encrypted text

E = a * P + b (mod N)

## Decryption

### Step 3: Decryption

Now, having our encrypted numbers, we want to perform the same procedure we used for encryption but in reverse. For this, we need to find the inverse of a.

### Step 3.1: Inverse of a

The process of obtaining the inverse of a is somewhat... simple?

It involves using an extended version of the Euclidean algorithm to find the quotients of the Greatest Common Divisor. With the results, we create a table somewhat like this:

|           |           | quotient 1 | quotient 2 | quotient 3 | quotient 4 |
|-----------|-----------|------------|------------|------------|------------|
|     0     |     1     |            |            |            |            |   
|     1     |     0     |            |            |            |            |

And by performing the process: quotient 1 * a_arr[i - 1] + a_arr[i - 2] where a_arr is the first row, we obtain the inverse of a.

### Step 3.2: Decryption

The decryption process for the AFFINE cipher is as follows:

P = plaintext
E = encrypted text

P = a^-1 * (E - b) (mod N)

## Step 4: Numbers to Letters

Finally, having our transformed numbers, we can convert them back into text, obtaining our desired text.

# Functions

## Letter to Number

## Number to Letter

## AFFINE_encrypt

## AFFINE_decrypt

## Inverse a

