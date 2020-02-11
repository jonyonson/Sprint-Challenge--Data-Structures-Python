import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# binary search tree
# runtime: 0.15756702423095703 seconds
# O(n log n)
# bst = BinarySearchTree(names_1[0])
# for name_1 in names_1[1:]:
#     bst.insert(name_1)

# for name_2 in names_2:
#     if bst.contains(name_2):
#         duplicates.append(name_2)

# set1 = set(names_1)
# set2 = set(names_2)
# duplicates = set1.intersection(set2)

names_2_set = set(names_2)
for name in names_1:
    if name in names_2_set:
        duplicates.append(name)



end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish with no restrictions on techniques or data
# structures?
