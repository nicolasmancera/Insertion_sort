def insertion_sort(lista):
	for p in range (1,len(lista)):
		valor=lista[p]
		i=p-1
		while i>=0:
			if valor < lista[i]:
				lista[i+1] = lista[i]
				lista[i]=valor
				i=i-1
			else:
				break