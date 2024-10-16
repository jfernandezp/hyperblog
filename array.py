array = ["Peru", 'Mexico', 'Francia', "Alemania", "Brazil", "Colombia", 'Chile']
index = array.index('Mexico')
array.append("Argentina")
array.insert(2, "Bolivia")
array.pop(1)
array.remove('Brazil')
array.extend('Uruguay')
array.reverse()
array.sort()
print(index)
for i in array:
    print(i)
