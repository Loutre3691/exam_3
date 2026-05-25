# Vérifie si les brackets d'une string sont correctement balancées.
# Gère : () [] {} — ordre et correspondance.

# Examples
# brackets("()") → True
# brackets("([])") → True
# brackets("(]") → False
# brackets("([)]") → False
# brackets("{[]}") → True


def brackets(text: str) -> bool:
	stack = []
	matching = {
       ')': '(',
       ']': '[',
       '}': '{'
	}
	for c in text:                              # on parcourt chaque caractère
		if c in '({[':                          # si c'est un ouvrant
			stack.append(c)                     # → on empile

		elif c in ')}]':                        # si c'est un fermant
			if not stack or stack[-1] != matching[c]:  # pile vide OU mauvais ouvrant
				return False                    # → impossible, on arrête tout
			stack.pop()                         # → ça correspond, on dépile

	return len(stack) == 0                      # pile vide = tout a été fermé ✅


if __name__ == "__main__":
   result = brackets("()")
   print(result)
   result_1 = brackets("([])")
   print(result_1)
   result_2 = brackets("(]")
   print(result_2)
   result_3 = brackets("([)]")
   print(result_3)
   result_4 = brackets("{[]}")
   print(result_4)