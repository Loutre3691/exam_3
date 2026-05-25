# Compte combien de fois deux chiffres consécutifs forment +1.
# Un caractère non-digit remet à zéro la séquence.

# Examples
# pattern_tracker("123") → 2
# pattern_tracker("1293") → 1
# pattern_tracker("a123b45") → 3
# pattern_tracker("0123456789") → 9

def pattern_tracker(text: str) -> int:
    result = ''.join(c for c in text if c.isdigit() and c != "0")
    return len(result)


if __name__ == "__main__":
    result1 = pattern_tracker("123")
    print(result1)
    result2 =pattern_tracker("1293")
    print(result2)
    result3 = pattern_tracker("a123b45")
    print(result3)
    result4 = pattern_tracker("0123456789")
    print(result4)