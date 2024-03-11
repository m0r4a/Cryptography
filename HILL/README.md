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
