tu = (1, 2.0, True, 1+2j, 'etl')
print("tuple values", tu)
print("type of tu is", type(tu))
print('memory of tu is', id(tu))

print("first element in tu is", tu[0], type(tu[0]), id(tu))
print("second element in tu is", tu[1], type(tu[1]), id(tu))
print("third element in tu is", tu[2], type(tu[2]), id(tu))
print("fourth element in tu is", tu[3], type(tu[3]), id(tu))
print("fifth element in tu is", tu[4], type(tu[4]), id(tu))

print("tu[1:3]", tu[1:3], type(tu[1:3]), id(tu[0:3]))

print("methods available in tuple type", dir(tu))


t2=(1,2,2,2,2,2,4,5,6,2,2,2,2,2)
print("count of 2", t2.count(2))
print("index of 4", t2.index(2))