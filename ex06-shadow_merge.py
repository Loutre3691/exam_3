# Fusionne deux listes et retourne une liste triée en ordre croissant.
# Interdit d'utiliser sort() directement.

# Examples
# shadow_merge([3,1,5], [2,4]) → [1,2,3,4,5]
# shadow_merge([], [1,2]) → [1,2]
# shadow_merge([-3,-1], [-5,0]) → [-5,-3,-1,0]


def shadow_merge(list1: list[int], list2: list[int]) -> list[int]:
    fusion = list1 + list2
    n = len(fusion)

    # Boucle 1 : On répète le tri pour être sûr que tout remonte
    for _ in range(n):
        # Boucle 2 : On s'arrête à n - 1 pour éviter que i + 1 ne sorte de la liste
        for i in range(n - 1):
            if fusion[i] > fusion[i + 1]:
                fusion[i], fusion[i + 1] = fusion[i + 1], fusion[i]

    return fusion

if __name__ == "__main__":
    result1 = shadow_merge([3,5,2], [4,1])
    print(result1)
    result2 = shadow_merge([], [1,2])
    print(result2)
    result3 = shadow_merge([-3,-1], [-5,0])
    print(result3)