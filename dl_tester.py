"""
    Double Linked List Tester
"""
from dl_list import DL_List

x = DL_List()
x.insert(10)
x.insert(20)
x.insert(-3)
x.insert(98)

#print(x.size())
print(x)
print(x.search(20))
print(x.search(99))
print(x.search(10))
print(x.search(44))