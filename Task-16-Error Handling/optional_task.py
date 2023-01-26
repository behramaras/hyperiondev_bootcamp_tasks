# There is a logical error. i is summed with i, not num.
# There is a runtime error. num_list has not index[10].

num = 0
num_list = ()

for i in range(10):
    i += i
    num_list.append(i)
    
print(num)
print(num_list[10])
