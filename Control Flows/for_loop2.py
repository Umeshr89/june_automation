# t = [1,2,3,4,5]
# t_squares=[]
#
# mul=1
# t = [1,2,3,4,5]
# for i in t:
#     mul = mul*i
#     print("mul ", mul)
#
# print(" mul ", mul)


ls = [1,2,3,4,5,6,7,8,9,10]
even_sum = 0
odd_sum = 0

for i in ls:
    if i % 2 == 0:
        even_sum = even_sum + i
    else:
        odd_sum = odd_sum + i

print("total value", even_sum+odd_sum)
print("even sum", even_sum)
print("odd_sum", odd_sum)

