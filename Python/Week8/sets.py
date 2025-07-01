#sets
''''
my_set = {1, 2, 3, 4, 5}
print(my_set)

my_set.add(6)
print(my_set)

my_set.remove(2)
print(my_set)
'''

my_set1 = {1, 2, 3, 4, 5}
my_set2 = {4, 5, 6, 7, 8}
#union joins 2 sets and removes duplicates
my_set3 = my_set1.union(my_set2)
print(my_set3)

#intersection returns only the common elements
inter_set = my_set1.intersection(my_set2)
print(inter_set)

#difference returns elements that are in my_set1 but not in my_set2
diff_set = my_set1.difference(my_set2)
print(diff_set)