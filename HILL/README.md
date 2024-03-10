# HILL Encryption and Decryption

The HILL encryption method is another encryption technique that I learned in my cryptography class. Here's how it works:

## Step 1: Variables

Similar to the AFFINE method, the HILL method also requires certain variables:

- n: the size of the matrix (usually a square matrix)
- K: the encryption key matrix
- P: the plaintext matrix
- C: the ciphertext matrix

Along with the plaintext string we want to encrypt.

## Step 2: Letters to Numbers

As with the AFFINE method, we need to convert the letters or the text string into numbers to operate on them.

## Encryption

### Step 3: Encryption

The encryption process for the HILL cipher involves matrix multiplication:

C = (P * K) mod n

## Decryption

### Step 3: Decryption

Similarly, the decryption process for the HILL cipher also involves matrix multiplication:

P = (C * K^-1) mod n

Where K^-1 is the inverse of the key matrix K.

## Step 4: Numbers to Letters

Finally, after decryption, we can convert the numerical results back into letters to obtain the plaintext.

# Functions

## Letter to Number

## Number to Letter

## HILL_encrypt

## HILL_decrypt

## Inverse of a matrix
