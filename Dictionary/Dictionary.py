# Dict : Changable | Ordered | no duplicate | {key : value} pair 
mydict = {1:'soyab',2:'rahul',3:'raj',4:'simran'}
# print(mydict) # len ,type

# accessing elements
# print(mydict[1]) 

# keys 
# for i in mydict:
#     print(i)

# accessing element using function
# print(mydict.get(1))
# print(mydict.values())
# print(mydict.keys())

# Updating
# mydict.update({5:'Sania'})
# print(mydict)

# Copying Dict
# thisdict = mydict.copy()
# print(thisdict)

# Changing 
# mydict.update({4:'Samar'})
# print(mydict)


# Deleting / Removing
# mydict.popitem()
# print(mydict)

# mydict.pop(2)
# print(mydict)

# mydict.clear()
# print(mydict)

# del mydict
# print(mydict)

# Creating Keys in Dict
# x = ('key1', 'key2', 'key3','key5')
# y = 0

# thisdict = dict.fromkeys(x, y)
# print(thisdict)

# Set default  same thorught
x = mydict.setdefault(1,'parth')
print(mydict)
print(x)