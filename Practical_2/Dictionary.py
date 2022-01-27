#20CE133 - Prachi Shah

#Write a Python script to check whether a given key already exists in a dictionary.
dic={"one":1 , "Two":2, "Three":3,"Four":4}
key1="one"
if key1 in dic:
    print(dic[key1], "key already exists in a dictionary.")
else:
    print("key not exists in a dictionary.")

#Write a Python script to merge two Python dictionaries.
dic1={'a':1,'b':2,'c':3}
dic2={'d':4,'e':5,'f':6}
dic=dic1.copy()
dic.update(dic2)
print(dic)

#Write a Python program to sum all the items in a dictionary.
print("Total Sum of values in the Dictionary : ",sum(dic.values()))

#Write a Python script to add a key to a dictionary.
dic = {0: 10, 1: 20}
dic.update({2:30})
print(dic)

#Write a Python script to concatenate following dictionaries to create a new one.
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic=dic1.copy()
dic.update(dic2)
dic.update(dic3)
print(dic)