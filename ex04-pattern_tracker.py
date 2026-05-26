# Écris une fonction qui compte le nombre de paires de chiffres consécutifs 
# valides dans une chaîne. Une paire valide est formée de deux chiffres adjacents 
# dont le second vaut exactement 
# un de plus que le premier. Un 9 suivi d’un 0 n’est PAS une paire valide.

# Examples
# pattern_tracker("123") → 2
# pattern_tracker("1293") → 1
# pattern_tracker("a123b45") → 3
# pattern_tracker("0123456789") → 9

def pattern_tracker(text: str) -> int:
    count = 0
    prev = None
    for c in text:
        if c.isdigit():
            if prev is not None and int(c) == prev + 1:   
                count += 1
            prev = int(c)
        else:
            prev = None

    return count


if __name__ == "__main__":
    result1 = pattern_tracker("123")
    print(result1)
    result2 =pattern_tracker("1293")
    print(result2)
    result3 = pattern_tracker("a123b45")
    print(result3)
    result4 = pattern_tracker("0123456789")
    print(result4)