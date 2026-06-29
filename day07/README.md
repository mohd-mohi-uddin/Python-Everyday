>>> DICTIONARIES:

the dictionarry is a data structutre which stores key value pairs.

student = {
    "name": "John",
    "age": 20,
    "grade": "A"
}

here the "name": is the key
"john" is the value

when u are typing a key makesure that its in its correct data type like if u need key as name sso use "" with name. 

>> how to pick an item from dictionary:

use syntax dictionary_name[key]

from above:

print(student["name"]) this is like list but in place of key we use index student[0].

>> adding a new entry to dictionary:

to do so same syntax
dictionary_name["key"] = "value"

here we need to assign value to the key assosiated with dictionary.

>> editing an item in the dictionary:

same as adding new item to dicionary but here the new value must be given.

dictionary_name["key"] = "new value" this will edit that particular item in the dictinary.

>> looping through dictionary:

for i in dictionary:
    print(i)   > here i is only the keys of dictionary
    print(dictionary[i])  >this will give u the values of that keys.

>> multiple if statements:

choose them only when we need every condition to be true.

>> nesting in lists:

you can nest a list inside a list.

["","","",'",["","",],""]
to get the char of nested list u can use double index [][].

>> nesting in dictionaries:

a dict is a data strucctur which can store large amount of data and u can nesta list inside dictionary and also u can nest a dict inside dict.

dict = {"a":[],"b":{ "c": []}}

>> built in functions for dict:

d = {}

d["name"] = "Asim"     # Add
d["name"] = "Ali"      # Update

print(d["name"])       # Access

print(d.keys())        # Keys
print(d.values())      # Values
print(d.items())       # Pairs

del d["name"]          # Delete

print(len(d))          # Size of keys


    