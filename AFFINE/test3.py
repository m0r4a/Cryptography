from functions.AFFINE_break import AFFINE_break

plain = "ABRILC"
encrypted = "AR^%%U"

n = 31
block_size = 3

print(f"Plain text: {plain}\n\nText we're looking for: {encrypted}")

AFFINE_break(plain, encrypted, n, block_size)
