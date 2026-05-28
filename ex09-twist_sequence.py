# Twist = déplace le dernier élément au début, décale les autres à droite.
# Applique k fois. Optimise avec mod pour les grands k.

# Examples
# twist_sequence([1,2,3,4], 1) → [4,1,2,3]
# twist_sequence([1,2,3,4], 2) → [3,4,1,2]
# twist_sequence([1,2,3,4], 4) → [1,2,3,4]


# def twist_sequence(arr: list[int], k: int) -> list[int]:
#     if not arr:  # securite si liste vide
#         return arr
    
#     k = k % len(arr)

#     for _ in range(k):
#         temp = arr.pop()    # supprime et retourne le dernier el avec pop qui est transferer dans temp
#         arr.insert(0, temp)     # insertion dans arr(a l'index 0) -> temp

#     return arr


def twist_sequence(arr: list, k: int) -> list:
    if not arr:
        return arr
    k = k % len(arr)
    return arr[-k:] + arr[:-k] if k else arr[:]

# arr = [1, 2, 3, 4]
# arr[-1:]  →  [4]          ← le dernier
# arr[:-1]  →  [1, 2, 3]   ← TOUT sauf le dernier



if __name__ == "__main__":
    result1 = twist_sequence([1,2,3,4], 1)
    print(result1)
    result2 = twist_sequence([1,2,3,4], 2)
    print(result2)
    result3 = twist_sequence([1,2,3,4], 9) 
    print(result3)