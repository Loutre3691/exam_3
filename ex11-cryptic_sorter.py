#  Trie une liste de strings selon 3 critères :
# ① longueur (courte → longue)  
# ② alphabétique (même longueur)  
# ③ nombre de voyelles (même longueur + même ordre alpha).

# Examples
# ["apple","cat","banana","dog","elephant"] → ["cat","dog","apple","banana","elephant"]
# ["aaa","bbb","AAA","BBB"] → ["AAA","aaa","BBB","bbb"]
# ["hello","world","hi","test"] → ["hi","test","hello","world"]
# [] → []

def cryptic_sorter(strings: list[str]) -> list[str]:
    def aeiou(s: str) -> int:
        return sum(1 for c in s.lower() if c in 'aeiou')

    return sorted(strings, key=lambda s: (len(s), s.lower(), aeiou(s)))


# ①len  ②alpha  ③voyelles
# "cat"  → (3,   "cat",    1)
# "dog"  → (3,   "dog",    1)
# "apple"→ (5,   "apple",  2)

# tri :
# (3, "cat", 1)   ← plus petit
# (3, "dog", 1)
# (5, "apple", 2) ← plus grand

# → ["cat", "dog", "apple"] ✅


if __name__ == "__main__":
    result1 = cryptic_sorter(["apple","cat","banana","dog","elephant"])
    print(result1)
    result2 = cryptic_sorter(["aaa","bbb","AAA","BBB"])
    print(result2)
    result3 = cryptic_sorter(["hello","world","hi","test"] )
    print(result3)
    result4 = cryptic_sorter([])
    print(result4)
