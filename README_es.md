# Mi clase de criptrografía y Python

## Introducción 

Este proyecto fue hecho para mi clase de criptografía en la universidad. Los examenes eran de varias horas los fines de semana, tediosos y aburridos, sin embargo, teníamos la opción de hacer los examenes mediante código así que decidi tomar ese camino.


## Objetivo

El objetivo principal de este proyecto fue simplemente tener un proyecto activo para seguir programando en Python.


## Contenido 

Este proyecto tiene 2 métodos de encriptación y un tema matemático relacionado con la criptografía.


<details>

<summary>Método de encriptación AFFINE</summary>

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


</details>

<details>

<summary>Método de encriptación HILL</summary>

# HILL Encryption and Decryption

The HILL encryption method is another encryption technique that I learned in my cryptography class. Here's how it works:

## Step 1: Variables

Similar to the AFFINE method, the HILL method also requires certain variables:

- n: the size of the alphabet
- m: the plaintext string
- matrix: the encryption key matrix

Some specific variables for this "project" are:

- matrix_size: The size of matrix you will be using
- block_size: A very straightforward variable 
- N: n ^ block_size, this is going to be the value of every mod operation 

## Step 2: Letters to Numbers

As with the AFFINE method, we need to convert the letters or the text string into numbers to operate on them.

## Encryption

### Step 3: Encryption

The encryption process for the HILL cipher involves matrix multiplication:

Being:
- C: Encrypted matrix
- P: Plain-text matrix

C = (P * K) mod n

## Decryption

### Step 3: Decryption

Similarly, the decryption process for the HILL cipher also involves matrix multiplication:

Being:
- C: Encrypted matrix
- P: Decrypted matrix

P = (C * K^-1) mod n

Where K^-1 is the inverse of the key matrix K.

## Step 4: Numbers to Letters

Finally, after decryption, we can convert the numerical results back into letters to obtain the plaintext.

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
- **Padding**: If necessary, it pads the string with 'A' characters to match the block size.

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

## list_to_HILL_np

This function converts a list of numbers into an array usable for Hill encryption.

### Parameters:

- `matrix_size` (*int*): The size of each sublist. This parameter determines the number of elements in each row of the resulting matrices.

- `numbers` (*list*): The list of numbers to be partitioned for transformation into matrices.

### Return Value:

The function returns a list of numpy matrices separated by sublists of size `matrix_size`.

### Functionality:

- **Partitioning Numbers**: The function divides the input list `numbers` into sublists of size `matrix_size`.

- **Reshaping into Matrices**: For each sublist, it creates a numpy array and reshapes it into a matrix with one row and the number of columns equal to the size of the sublist.

- **List of Matrices**: The resulting matrices are collected into a list.

### Example Usage:

```python
# Example Usage
import numpy as np

# Define input parameters
matrix_size = 2
numbers = [1, 2, 3, 4, 5, 6]

result = list_to_HILL_np(matrix_size=matrix_size, numbers=numbers)
print(result)
```

#### Output: [array([[1, 2]]), array([[3, 4]]), array([[5, 6]])]


## matrix_multiplication_HILL_np

This function performs matrix multiplication for the Hill encryption method.

### Parameters:

- `N` (*int*): The size of the alphabet raised to the power of the block size. This parameter is crucial for modulo operation during matrix multiplication.

- `matrices` (*list*): A list of numpy matrices. These matrices represent the transformation matrices used in Hill encryption.

- `matrix` (*np.ndarray*): The matrix to be multiplied with each matrix in the list. This matrix typically represents the plaintext or ciphertext.

### Return Value:

The function returns a list of numpy matrices resulting from the multiplication.

### Functionality:

- **Matrix Multiplication**: The function iterates over each matrix in the `matrices` list and performs matrix multiplication with the input `matrix`. It uses NumPy's `dot` function for matrix multiplication.

- **Modulo Operation**: After each multiplication, the result is taken modulo `N` to ensure it stays within the bounds defined by the Hill encryption method.

- **Flatten and Convert to List**: The resulting matrices are flattened and converted to lists using NumPy's `flatten` method and `tolist` function. This step is necessary to return the result in a format compatible with the expected output.

### Example Usage:

```python
# Example Usage
import numpy as np

# Define matrices and matrix
matrices = [np.array([[1, 2], [3, 4]]), np.array([[5, 6], [7, 8]])]
matrix = np.array([[1, 0], [0, 1]])

result = matrix_multiplication_HILL(N=26, matrices=matrices, matrix=matrix)
print(result)
```
#### Output: [[1, 2, 3, 4], [5, 6, 7, 8]] 


## matrix_inverse_HILL

This function calculates the inverse of a matrix for the Hill encryption method.

### Parameters:

- `N` (*int*): The size of the alphabet raised to the power of the block size (modulo value).
- `matrix` (*np.ndarray*): The matrix to be inverted.

### Return Value:

The function returns the inverse of the input matrix modulo N.

### Functionality:

- **Calculate Determinant Modulo**: It calculates the determinant of the input matrix modulo N.
- **Calculate Adjoint Modulo**: It computes the adjoint of the input matrix modulo N.
- **Calculate Inverse**: It calculates the modular inverse of the determinant modulo N.
- **Calculate Inverse Matrix**: The inverse of the input matrix is then computed using the adjoint and the modular inverse of the determinant.
- **Error Handling**: If the input matrix is not invertible, a message is printed, and `None` is returned.

#### Subfunctions:

### Determinant Modulo

This function calculates the determinant of a matrix modulo N.

### Parameters:

- `matrix`: The matrix for which the determinant will be calculated.
- `N`: The modulo value.

### Return Value:

The function returns the determinant of the matrix modulo N.

### Functionality:

- **Calculate Determinant**: It computes the determinant of the input matrix.
- **Modulo Operation**: The determinant value is then rounded, converted to an integer, and taken modulo N to ensure it stays within the bounds defined by the Hill encryption method.

### Adjoint Modulo

This function computes the adjoint of a matrix modulo N.

### Parameters:

- `matrix`: The matrix for which the adjoint will be calculated.
- `N`: The modulo value.

### Return Value:

The function returns the adjoint of the matrix modulo N.

### Functionality:

- **Calculate Adjoint**: It calculates the inverse of the input matrix, multiplies it by the determinant of the original matrix, and rounds the result.
- **Modulo Operation**: The resulting adjoint matrix is then converted to integer type and taken modulo N to ensure it stays within the bounds defined by the Hill encryption method.

#### Example Usage:

```python
# Example Usage
import numpy as np

# Define input parameters
N = 26
matrix = np.array([[4, 3], [3, 2]])

result = matrix_inverse_HILL(N=26, matrix=matrix)
print(result)
```

##### Output: [[13 20], [20  9]]


</details>

<details>

<summary>Congruencias Lineales</summary>

# Linear Congruence Resolution using Chinese Remainder Theorem

The Chinese Remainder Theorem (CRT) is a fundamental result in number theory, particularly useful in solving systems of linear congruences. Let's understand how it works:

## Introduction

When faced with a system of congruences of the form:

x ≡ a_1 (mod m_1)
x ≡ a_2 (mod m_2)
...
x ≡ a_n (mod m_n)

Where `a_i` and `m_i` are integers, the Chinese Remainder Theorem provides a method to find a solution `x` that satisfies all the congruences simultaneously.

## Method

Given a system of congruences, the CRT proceeds as follows:

1. **Initialization**: We start with congruences of the form `x ≡ a_1 (mod m_1)` and `x ≡ a_2 (mod m_2)`.
2. **Solution of Two Congruences**: If we have two congruences, we can find the solution for `x`.
3. **Extension to Three Congruences**: If we have three congruences, we extend the solution by finding `x` that satisfies all three congruences.
4. **Generalization to N Congruences**: The process can be extended to any number of congruences.
5. **Final Solution**: The final solution is obtained by taking the result modulo the product of the moduli of all congruences.

## Example

Consider the following system of congruences:

x ≡ 2 (mod 3)
x ≡ 3 (mod 7)
x ≡ 4 (mod 16)

Using the Chinese Remainder Theorem, we can solve this system and obtain the value of `x` that satisfies all three congruences.

The value of `x` satisfying all three congruences is `164`.

This illustrates how the Chinese Remainder Theorem can efficiently solve systems of congruences, a fundamental technique in number theory and cryptography.

## Note 

I relied entirely on the sympy library to do the sequence resolution due to lack of time, however, if I decide to take this project further, everything will eventually be programmed manually.


</details>

_Nota: Los README están en ingles, esos no pienso traducirlos en un futuro cercano._


## Aprendizaje, dificultades y el abandono del proyecto

### Criptografía

En términos de criptografía práctica, útil o aplicable realmente aprendí poco, solo aprendí en profundidad estos dos métodos de encriptación y desde un punto de vista matemático, no práctico.

### Python 

Para Python aprendí bastante, creo que mi nivel como "programador" subió, aprendí a usar los docstrings, a hacer un README.md "decente", utilicé argparse bastante, aprendí un poco de la librería numpy, etc. 

### Dificultades

La mayor dificultad fue la mala planificación a futuro del proyecto, como se refleja en la carpeta .old, esas fueron las versiones pasadas de este proyecto antes de practicamente rehacerlo todo. 

Ahora tendré que tener bastante más en cuenta la planificación de mis proyectos, entre más "a la izquierda" se encuentre un error en el desarrollo de un proyecto, más fácil será corregirlo.

### Abandono del proyecto

Al final abandoné este proyecto ya que no había incentivo para seguir trabajando en el, al final los requisitos para los examenes fueron cambiados indiscriminadamente y no se me permitió hacer los examenes compeltamente mediante código y sin poder hacerlos de esa forma ya no tenía sentido ni razón de ser el utilizar tantas horas de mi tiempo en programar este proyecto.


## Conclusión

Después de haber hecho este proyecto me dejé de sentir oxidado en Python, aprendí un poco de criptografía y me di cuenta de la importancia de la planificación en un proyecto, aunque lo dejo aquí como un proyecto abandonado, me siento satisfecho con el resultado y con todo lo que aprendí en el proceso.
