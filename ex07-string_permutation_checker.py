# Vérifie si deux strings sont des permutations l'une de l'autre.
# Mêmes caractères, mêmes occurrences, ordre différent.

# Examples
# ("abc", "cab") → True
# ("hello", "olleh") → True
# ("abc", "abcc") → False
# ("listen", "silent") → True

def string_permutation_checker(s1: str, s2: str) -> bool:
    return sorted(s1) == sorted(s2)

if __name__ == "__main__":
    result1 = string_permutation_checker("abc", "cab")
    print(result1)
    result2 = string_permutation_checker("hello", "olleh")
    print(result2)
    result3 = string_permutation_checker("acb2", "a2bc")
    print(result3)
    result4 = string_permutation_checker("listen", "silent")
    print(result4)