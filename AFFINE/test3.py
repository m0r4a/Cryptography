from functions.AFFINE_break import AFFINE_break

plain = "RAULMORAAGUIRRE"
encrypted = "BIBBN$BA%LGYHDL"
n = 31
block_size = 3

print("------ ENCRYPTING ------\n\nText: ", plain)
AFFINE_break(plain, encrypted, n, block_size)
