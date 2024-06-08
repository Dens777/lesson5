immutable_var=10,8,1979,"download",False,"overload"
print(immutable_var)
print(type(immutable_var))
mutable_list=[10,8,1979,"download",False,"overload"]
print(mutable_list)
print(type(mutable_list))
mutable_list=[10,8,1979,"download",False,"overload"]
mutable_list=[10,8,1979,"download",False,"overload"]
index = mutable_list.index("overload")
mutable_list[index] = "normal"
print(mutable_list)

