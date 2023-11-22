
arr1 = [1,2,3,4,5]
arr2 = [4,5,6,7,8,]
set1 = set(arr1)
set2 = set(arr2)
set_interscection = set1.intersection(set2)
print("set1", set1)
print("set2", set2)
'''
set1.add(6)
set1.remove(1)
print(set1)
print(1 in set1)
'''
set_overlap = set1 & set2
print("overlap: ",set_overlap)
print("diff in 1: ",set1.difference(set2) )
print("intersection: ",set1.intersection(set2) )
print("union: ",set1.union(set2) )
print("is inter a 1 subset: ",set_interscection.issubset(set2) )
print("is 1 a inter super set: ",set1.issuperset(set_interscection) )

