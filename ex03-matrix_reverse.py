# Retourne une nouvelle matrice où chaque ligne est inversée.
# La matrice originale ne doit pas être modifiée.

# Examples
# [[1,2,3],[4,5,6]] → [[3,2,1],[6,5,4]]
# [[1,2],[3,4]] → [[2,1],[4,3]]
# [[1]] → [[1]]

def matrix_reverse(matrix: list) -> list:
    return [row[::-1] for row in matrix]

if __name__ == "__main__":
    matrix = [
        [1,2,3],
        [4,5,6]
    ]
    result = matrix_reverse(matrix)
    print(result)