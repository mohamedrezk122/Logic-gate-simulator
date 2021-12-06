
def AND(*args):

	return int(all(*args))


def OR(*args):

	return int(any(*args))


def NOT(a):

	return int(not a)


def XOR(*args):

	lst = []
	print()
	for i in args:
		for j in range(len(i)):
			#print(j)
			lst.append(args[0][j])


	if lst.count(1) %2 != 0 :

		return 1

	else:
		return 0 	


def NAND(*args):

	return NOT(AND(*args))


def NOR(*args):

	return NOT(OR(*args))


def XNOR(*args):

	return NOT(XOR(*args))


if __name__ == "__main__" :

	print(XNOR((0,1,1)))