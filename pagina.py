def linter(caracter):
	try:
		parentesis = []
		for c in caracter:
			if c == '(':
				parentesis.append(c)
			elif c == ')':
				temp = parentesis.pop()
				if c != '(':
					return False
			elif c == '[':
				parentesis.append(c)
			elif c == ']':
				temp = parentesis.pop()
				if c != '[':
					return False
		return len(parentesis) == 0
	except:
		return False


print(linter(input()))
