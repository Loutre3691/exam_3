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
    
# base = ord('A') = 65

# ① ord('H')        = 72        ← position ASCII de H
# ② 72 - 65         = 7         ← position dans l'alphabet (0=A, 1=B...)
# ③ 7 + 3           = 10        ← on décale de 3
# ④ 10 % 26         = 10        ← wrap (reste dans 0-25)
# ⑤ 10 + 65         = 75        ← on remet en ASCII
# ⑥ chr(75)         = 'K'  ✅


# base = ord('a') = 97

# ① ord('z')        = 122       ← position ASCII de z
# ② 122 - 97        = 25        ← position dans l'alphabet (0=a ... 25=z)
# ③ 25 + 3          = 28        ← on décale de 3
# ④ 28 % 26         = 2         ← wrap ! 28 = 1×26 + 2, il reste 2
# ⑤ 2 + 97          = 99        ← on remet en ASCII
# ⑥ chr(99)         = 'c'  ✅


if __name__ == "__main__":
    result1 = whisper_cipher("Hello", 3)
    print(result1)
    result2 = whisper_cipher("xyz", 3) 
    print(result2)
    result3 = whisper_cipher("Hello", 13) 
    print(result3)
    result4 = whisper_cipher("abc", -1)
    print(result4)
    


