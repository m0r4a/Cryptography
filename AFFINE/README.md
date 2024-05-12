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

This function transforms letters into numbers based on the Hill encryption method.

### Parameters:

- `alphabet_size` (*int*): The size of the alphabet, i.e., the number of characters in the alphabet. This parameter is crucial for calculating the base for converting characters into their corresponding numeric values.

- `block_size` (*int*): The size of each block or "level" in the graph. This parameter determines how the input string is divided into blocks for processing.

- `string` (*str*): The string to be converted into numbers. It's the input data that needs to undergo the transformation.

### Return Value:

The function returns a list of integers representing the numeric values obtained from the letters in the input string.

### Functionality:

- **Divide the String into Blocks**: The input string is divided into blocks of the specified size using list comprehension. Each block represents a segment of the input data.

- **Convert Characters to Numeric Values**: For each block, the function iterates through the characters in reverse order (from right to left). Inside this loop, it calls the `char_to_number` function to convert each character into its corresponding numeric value based on the alphabet size.

- **Calculate Decimal Values**: It calculates the decimal value of each block using the formula: `decimal_value += numeric_value * (alphabet_size ** i)`, where `i` represents the position of the character in the block.

- **Collect Decimal Values**: Finally, it appends the decimal value of each block to a list and returns this list of decimal values as the output.

### Example Usage:

```python
# Example Usage
result = letter_to_number(alphabet_size=26, block_size=2, string="HELLOZ")
print(result)
```
#### Output: [186, 297, 389]

## Number to Letter

This function transforms numbers into letters according to the AFIN encryption method.

### Parameters:

- `alphabet_size` (*int*): The number of characters in the alphabet.
- `block_size` (*int*): The size of each block or "level" in the graph.
- `decimal_values` (*str or list or list of lists*): The numbers to be transformed into letters. It can be a single string, a list of numbers, or a list of lists of numbers.

### Return Value:

The function returns the letters obtained from the input numbers.

### Functionality:

- **Prepare Decimal Values**: It ensures that the input `decimal_values` are in the correct format (a flat list of numbers).
- **Convert Numbers to Letters**: For each number in the input, it converts it into a string of letters based on the alphabet size and block size.

### Example Usage:

```python
# Example Usage
alphabet_size = 26
block_size = 2
decimal_values = [1, 2, 3, 4]

result = number_to_letter(alphabet_size=alphabet_size, block_size=block_size, decimal_values=decimal_values)
print(result)
```

#### Output: "BA DC"

## AFFINE_encrypt

This function performs encryption using the AFFINE method, which is a type of substitution cipher. The AFFINE method encrypts using a mathematical function (ax + b) where 'a' and 'b' are the keys of the cipher.

### Parameters:

- `-N` (*int*): Alphabet size raised to the power of the block size. It determines the modulus for encryption, ensuring that the result falls within the range of the alphabet.
  
- `-a` (*int*): The 'a' value in the encryption formula [a, b] = [x, y], where 'a' is the coefficient applied to the input number.
  
- `-b` (*int*): The 'b' value in the encryption formula [a, b] = [x, y], where 'b' is the constant added to the result after multiplication.
  
- `-m` (*int*): The number to be encrypted using the AFFINE method.

### Return Value:

The function prints the encrypted message obtained after applying the AFFINE encryption method to the input number.

### Functionality:

- **Argument Processing**: The function processes command-line arguments provided by the user, ensuring all required arguments (-N, -a, -b, and -m) are present.
  
- **AFFINE Encryption**: The `AFFINE_encrypt` function encrypts the input number using the AFFINE method. It performs the encryption operation (ax + b) mod N, where 'a' and 'b' are the keys, 'x' is the input number, 'N' is the modulus, and 'mod' denotes the modulo operation.
  
- **Handling Single or Multiple Numbers**: The function handles both single numbers and lists of numbers provided as input for encryption.


## AFFINE_decrypt

This function decrypts a number encrypted by the AFFINE method, which is a type of substitution cipher. The AFFINE method uses a mathematical function to encrypt and decrypt data.

### Parameters:

- `-N` (*int*): Alphabet size raised to the power of the block size. It represents the modulus used during encryption.
  
- `-a` (*int*): The inverse of 'a' used during encryption. It's the value of 'a' after applying the inverse function.
  
- `-b` (*int*): The original 'b' value used during encryption. It's the constant added during encryption.
  
- `-m` (*str*): The encrypted numbers to decrypt, separated by commas.

### Return Value:

The function prints the decrypted numbers obtained after applying the inverse operation to the input encrypted numbers.

### Functionality:

- **Argument Processing**: The function processes command-line arguments provided by the user, ensuring all required arguments (-N, -a, -b, and -m) are present.
  
- **AFFINE Decryption**: The `AFFINE_decrypt` function decrypts the input numbers using the AFFINE method. It applies the inverse function (a_inverse * (number - original_b)) mod N to each encrypted number to obtain the decrypted value.
  
- **Handling Single or Multiple Numbers**: The function handles both single numbers and lists of numbers provided as input for decryption.


## Inverse a

This function finds the inverse of a number 'x' using the Extended Euclidean algorithm. The algorithm is used to find the greatest common divisor (GCD) of two integers and compute integers 'a' and 'b' such that a*x + b*y = GCD(x, y).

### Parameters:

- `-a` (*int*): The first number (x) for which the inverse is to be found.
  
- `-N` (*int*): The alphabet size raised to the power of the block size (n ^ block_size). It's the modulus used in the calculation.

### Return Value:

The function prints the inverse of the input number 'x' obtained using the Extended Euclidean algorithm.

### Functionality:

- **Argument Processing**: The function processes command-line arguments provided by the user, ensuring all required arguments (-a and -N) are present.
  
- **Extended Euclidean Algorithm**: The `inverse_a` function implements the Extended Euclidean algorithm to find the inverse of the input number 'x'. It performs a series of steps involving division and modular arithmetic until the GCD of 'x' and 'N' is found, leading to the determination of the inverse.
  
- **Table Creation**: The function creates a table of intermediate values during the algorithm's execution to aid in the computation and visualization of the process.

## AFFINE_break

This function bruteforces the values of 'a' and 'b' given an affine encryption, exploiting the property that 'a' must be coprime to 'N', significantly reducing the search space.

### Parameters:

- `n` (*int*): The alphabet size.
  
- `block_size` (*int*): The level of the graph being used.
  
- `plain_text` (*str*): The known plain text of the letters.
  
- `encrypted_text` (*str*): The encrypted text obtained.

### Return Value:

The function prints the possible values of 'a' and 'b' that could have been used for the encryption.

### Functionality:

- **Coprime Values**: The function generates a list of coprime values of 'N' to reduce the amount of testing required for 'a'.
  
- **Bruteforce Search**: It iterates through possible combinations of 'a' and 'b' within defined ranges to find a match between the encrypted message obtained and the expected encrypted text.
  
- **Encryption and Decryption**: The function encrypts the known plain text using the current values of 'a' and 'b' and checks if the resulting encrypted message matches the provided encrypted text.
  
- **Output Display**: If a match is found, the function prints the possible values of 'a' and 'b'. Otherwise, it indicates that no possible values were found.

### Example Usage:

```python
plain_text = "HELLOZ"
encrypted_text = "BA DC"
alphabet_size = 26
block_size = 2

AFFINE_break(plain_text, encrypted_text, alphabet_size, block_size)
```

### Output:

--- Match 1 ---
Possible value for a: 3
Possible value for b: 7
