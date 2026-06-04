# Écris une fonction qui convertit un nombre d'une base vers une autre.
# Prends en charge les bases de 2 à 36 inclus, avec les chiffres 0-9
#  et les lettres A-Z pour les valeurs 10-35. Renvoie "ERROR" pour les 
#  entrées invalides (base, chiffres).

#Examples

# ("101", 2, 10) → "5"
# ("FF", 16, 10) → "255"
# ("255", 10, 16) → "FF"
# ("XYZ", 10, 2) → "ERROR"

def number_base_converter(number: str, from_base: int, to_base: int) -> str:
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    try:                 # Si digits.index(c) ne trouve pas c → ValueError → on retourne "ERROR"
        decimal = int(number, from_base)   # Conversion auto avec int qui transofmre la str avec la base, calcul auto
        if decimal == 0:       # Si le nombre vaut 0, la boucle while ne s'exécuterait jamais
            return "0"
        result = ""
        while decimal:      # Tant que decimal > 0 (while 0 = False → s'arrête)
            result = digits[decimal % to_base] + result
            decimal //= to_base      # // = division ENTIÈRE (pas de virgule !)
        return result
    
    except ValueError:
        return "ERROR" 
    
if __name__ == "__main__":
    result1 = number_base_converter("11", 2, 10)
    print(result1)
    result2 = number_base_converter("ff", 16, 10)
    print(result2)
    result3 = number_base_converter("455", 10, 10)
    print(result3)
    result4 = number_base_converter("XYZ", 10, 16)
    print(result4)
    result5 = number_base_converter("1111", 2, 10)
    print(result5)