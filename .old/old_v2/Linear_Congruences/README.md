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
