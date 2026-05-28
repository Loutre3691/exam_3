# Chiffre de César : décale chaque lettre de shift positions.
# Préserve la casse, ignore les non-alphabétiques, wrap autour de l'alphabet.

# Examples
# whisper_cipher("Hello", 3) → "Khoor"
# whisper_cipher("xyz", 3) → "abc"
# whisper_cipher("Hello", 13) → "Uryyb"
# whisper_cipher("abc", -1) → "zab"

def whisper_cipher(text: str, shift: int) -> str:
    result =  ""
    for c in text:
        if c.isalpha():
            base = ord("a") if c.islower() else ord("A")
            result += chr((ord(c) - base + shift) % 26 + base)
        else:
            result += c

    return result
    

if __name__ == "__main__":
    result1 = whisper_cipher("Hello", 3)
    print(result1)
    result2 = whisper_cipher("xyz", 3) 
    print(result2)
    result3 = whisper_cipher("Hello", 13) 
    print(result3)
    result4 = whisper_cipher("abc", -1)
    print(result4)
    


