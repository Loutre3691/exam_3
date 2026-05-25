# EXERCISE 02 : echo_validator
# Vérifie si une string est un palindrome.
# Ignore les caractères non-alphabétiques et la casse.

# Examples
# echo_validator("Radar") → True
# echo_validator("A man a plan…") → True
# echo_validator("Hello") → False
# echo_validator("racecar") → True

def echo_validator(text: str) -> bool:
    cleaned = ''.join(c.lower() for c in text if c.isalpha())
    return cleaned == cleaned[::-1]

# "radar"[0:5:1]    → "radar"   (du début à la fin, un par un)
# "radar"[0:5:2]    → "rdr"     (un caractère sur deux)
#  "radar"[::-1]    → "radar"   (de la fin au début, à l'envers) 


if __name__ == "__main__":
    result1 = echo_validator("racecar")
    print(result1)
    result2 = echo_validator("Hello")
    print(result2)
    result3 = echo_validator("A man a plan a canal: Panama")
    print(result3)
    result4 = echo_validator("Radar")
    print(result4)