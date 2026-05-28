# Indices pairs → lowercase, indices impairs → uppercase.
# Les caractères non-alphabétiques sont ignorés dans le comptage.

# Examples
# py_string_sculptor("Hello World") → "hElLo WoRlD"
# py_string_sculptor("HELLO") → "hElLo"
# py_string_sculptor("a1b2c3") → "a1B2c3"

def py_string_sculptor(text: str) -> str:
    result = ""
    pair = 0

    for c in text:
        if c.isalpha():
            if pair % 2 == 0:
                result += c.lower()
            else:
                result += c.upper()
            pair += 1
        else:
            result += c

    return result

if __name__ == "__main__":
    result1 = py_string_sculptor("Hello World") 
    print(result1)
    result2 = py_string_sculptor("HELLO")
    print(result2)
    result3 = py_string_sculptor("a1b2c3")
    print(result3)