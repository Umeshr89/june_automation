s = {1, 2.0, True, 1+2j, 'etl',False,0,1}

print("set of values", s)
print("type of s is", type(s))
print("memory of s", id(s))

#print(s[0])

print("methods available in sets", dir(s))

ls=[1,2,2,3,2]

ls = set(ls)

print(list (ls))

s1 = {1,2,3,4}

s2={3,4,5}

print("s1.intersection(s2", s1.intersection(s2))
print("s.intersection(s2", s1.difference(s2))

s1.add(8)

#print("s1 after add", s1)

s.pop()
print("s1after pop", s1)


fs = frozenset(s1)

print("fs set values", fs)
print("type of fs is", type(fs))
print("memory of fs is", id(fs))
print("methods available in fs", dir(fs))
