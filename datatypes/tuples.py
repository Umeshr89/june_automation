ls2 = [1, 2.0, True, 1+2j, 'etl', [1,2], (1,2)]

print("list of values", ls2)
print("type of ls is", type(ls2))
print("memory of ls", id(ls2))


print("first element in ls is", ls2[0], type)

#append insert extend
print("ls2 before append", ls2)
ls2.append(24.5)
print("ls2 after append", ls2)
ls2.append('etl')

