from sympy.ntheory.modular import solve_congruence


def solve_congruences(arr1, arr2, arr3=None):
    if arr3:
        # Solución de tres congruencias
        x = solve_congruence((arr1[0], arr1[1]), (arr2[0], arr2[1]), (arr3[0], arr3[1]))[0]
        return x % (arr1[1] * arr2[1] * arr3[1])
    else:
        # Solución de dos congruencias
        x = solve_congruence((arr1[0], arr1[1]), (arr2[0], arr2[1]))[0]
        return x % (arr1[1] * arr2[1])


arr1 = [3, 7]
arr2 = [4, 9]

answer = solve_congruences(arr1, arr2)

print(answer)
