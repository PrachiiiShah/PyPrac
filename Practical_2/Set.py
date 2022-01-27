#20CE133 - Prachi Shah

#Write a Python program to add member(s) in a set and clear a set
from pickle import TUPLE1
from typing import Counter


set={'w','o','r','l','d'}
print("SET is : ",set)
set.add("!")
print("SET before clear : ", set)
print("SET after clear : ", set.clear())

#Write a Python program to remove an item from a set if it is present in the set.
set={'w','o','r','l','d'}
set.remove('l')
print("After remove l : " ,set)

#Write a Python program to create an intersection, Union, difference of sets.
set1={1,2,3,4}
set2={3,4,5,7}
print("Union of se1 and set2 is : ",set1.union(set2))
print("Intersection of set1 and set2 is : ", set1.intersection(set2))
print("Difference between set1 and set2 is : ",set1.difference(set2))

#Write a Python program to find maximum and the minimum value in a set.
set={1,2,3,4,5}
print("Maximum Number is : ",max(set))
print("Minimum Number is : ",min(set))

#Write a Python program to find the most common elements and their counts from list, tuple, dictionary.
list1=['apple','orange','banana','apple','apple','apple','apple','orange']
most_common=max(list1,key=list1.count)
print("Most Common Element in List : ",most_common ,list1.count(most_common) ,"times")
    
"""def intersection(A, B, C):
    s1 = set(A)
    s2 = set(B)
    s3 = set(C)
    print("List =", A)
    print("Tuple =", B)
    print("Dictionary =", C)
    set1 = s1.intersection(s2)
    result_set = set1.intersection(s3)
    final_list = list(result_set)

    print("Common of members of list, tuple and dictionary:", final_list)

if __name__== "__main__":
    list1 = [1, 2, "ABC", 3.4]
    tuple1 = (12, 20, "ABC", 3.4)
    dictionary1 = {"ABC", 1, 3.4, "PQR"}
    intersection(list1, tuple1, dictionary1)"""
